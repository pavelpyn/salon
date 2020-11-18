from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import FormView
from .forms import ReviewForm, FeedbackForm
from .models import Review, Contacts, Feedback, Sale, Masters


def base_page(request):
    contact = Contacts.objects.all()
    context_contacts = {'contact': contact}
    return render(request, 'main/base.html', context_contacts)


def index(request):
    error = ''
    reviews = Review.objects.filter(done='True').order_by('-created')
    example = Masters.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/reviews')
        else:
            error = 'Форма была неверной'
    form = ReviewForm()
    reviews_index = {
        'reviews': reviews,
        'form': form,
        'error': error,
        'example': example}
    return render(request, 'main/index.html', reviews_index)


def about(request):
    contacts = Contacts.objects.all()
    context_contacts = {'contacts': contacts}
    return render(request, 'main/about.html', context_contacts)


def other_page(request, page):
    try:
        template = get_template('main/' + page + ".html")
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


def reviews_list(request):
    error = ''
    reviews = Review.objects.filter(done='True').order_by('-created')
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/reviews')
        else:
            error = 'Форма была неверной'
    form = ReviewForm()
    context_review = {
        'reviews': reviews,
        'form': form,
        'error': error}
    return render(request, 'main/reviews.html', context_review)


def contacts(request):
    contact = Contacts.objects.all()
    context_contacts = {'contact': contact}
    return render(request, 'main/contacts.html', context_contacts)


def feedback(request):
    error = ''
    feedback = Feedback.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = FeedbackForm()
    context_feedback = {
        'feedback': feedback,
        'form': form,
        'error': error}
    return render(request, 'main/feedback.html', context_feedback)


def sale(request):
    sales = Sale.objects.all()
    context_sales = {'sales': sales}
    return render(request, 'main/sale.html', context_sales)


def masters(request):
    master_1 = Masters.objects.filter(tag='master_1')
    master_2 = Masters.objects.filter(tag='master_2')
    context_master = {'master_1': master_1, 'master_2': master_2}
    return render(request, 'main/masters.html', context_master)


def masters_1(request):
    master_1 = Masters.objects.filter(tag='master_1')
    context_master = {'master_1': master_1}
    return render(request, 'main/masters_1.html', context_master)


def masters_2(request):
    master_2 = Masters.objects.filter(tag='master_2')
    context_master = {'master_2': master_2}
    return render(request, 'main/masters_2.html', context_master)


def examples(request):
    example = Masters.objects.all()
    context_examples = {'example': example}
    return render(request, 'main/examples.html', context_examples)