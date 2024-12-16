from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Session
import random


# Create your views here.
@login_required
def start(request):
    # Fetch only sessions belonging to the logged-in user
    sessions = Session.objects.filter(user=request.user, is_completed=False)
    return render(request, 'quiz/main.html', {'previous_sessions': sessions})

@login_required
def create_session(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        session = Session.objects.create(name=name, user=request.user)

        # Pick 10 random questions and assign them to the session
        questions = list(Question.objects.all())
        selected_questions = random.sample(questions, min(10, len(questions)))
        session.questions.set(selected_questions)
        session.save()

        return redirect('play_session', session_id=session.id)

@login_required
def play_session(request, session_id):
    session = get_object_or_404(Session, id=session_id, user=request.user)

    if request.method == 'POST':
        # Save progress
        for question in session.questions.all():
            answer = request.POST.get(f'question_{question.id}')
            if answer:
                session.progress[str(question.id)] = answer
        session.save()
        if request.POST.get('action') == 'save':
            messages.success(request, "Session progress saved successfully!")
            return redirect('start')
        else:
            return redirect('submit_session', session_id=session.id)

    # Render all questions
    questions = session.questions.all()
    return render(request, 'quiz/play_session.html', {
        'session': session,
        'questions': questions,
        'progress': session.progress,
    })

@login_required
def submit_session(request, session_id):

    session = get_object_or_404(Session, id=session_id, user=request.user)

    if request.method == 'POST':
        # Save progress
        for question in session.questions.all():
            answer = request.POST.get(f'question_{question.id}')
            if answer:
                session.progress[str(question.id)] = answer
        session.save()

    # Mark session as completed
    session.is_completed = True
    session.save()

    return redirect('show_results', session_id=session.id)

@login_required
def show_results(request, session_id):
    session = get_object_or_404(Session, id=session_id, user=request.user)
    questions = session.questions.all()
    progress = session.progress
    correct_count = 0

    for question in questions:
        if progress.get(str(question.id)) == question.correct_option:
            correct_count += 1

    return render(request, 'quiz/results.html', {
        'session': session,
        'questions': questions,
        'progress': progress,
        'correct_count': correct_count,
        'total_questions': len(questions),
    })
