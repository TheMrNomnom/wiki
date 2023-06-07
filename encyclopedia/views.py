from django.shortcuts import render

from . import util

from markdown2 import Markdown

from django.http import HttpResponseRedirect
from django.urls import reverse
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "All Pages"
    })

def wiki(request, title):
    markdowner = Markdown()
    if not title:
        return HttpResponseRedirect(reverse("encyclopedia:index"))

    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "error_title": "No Wiki Entry Found",
            "error_message": f"No entry named {title} found"
        })
    else:
        md_result = util.get_entry(title)
    title_page = markdowner.convert(md_result)

    return render(request, "encyclopedia/wiki.html", {
        "title": title,
        "title_page": title_page
    })

def search(request):
    if request.method == "GET":
        search_query = request.GET.get('q')

        if search_query == '':
            search_query = 'None'

    titles = util.list_entries()
    search_results = []
    search_query_lower = search_query.lower()
    for title in titles:
        title_lower = title.lower()
        if search_query_lower == title_lower:
            return HttpResponseRedirect(reverse("wiki", kwargs={'title':title}))

        if search_query_lower in title_lower:
            search_results.append(title)

    return render(request, "encyclopedia/index.html", {
        "entries": search_results,
        "title": "Search Results"
    })

def create_new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_entry.html")


    if request.method == "POST":
        new_title = request.POST.get("new_title")

        if new_title == "":
            return render(request, "encyclopedia/error.html", {
                "error_title": "No New Entry Title",
                "error_message": "No title provided for new entry"
            })

        titles = util.list_entries()
        new_title_lower = new_title.lower()
        for title in titles:
            if new_title_lower == title.lower():
                return render(request, "encyclopedia/error.html", {
                    "error_title": "Entry Already Exists",
                    "error_message": f"Entry with the title {title} already exists."
                })

        new_entry_text = request.POST.get("new_entry_text")

        util.save_entry(new_title, new_entry_text)

        return HttpResponseRedirect(reverse("wiki", kwargs={'title':new_title}))

def edit_page(request, current_title):
    if request.method == "GET":
        md_result = util.get_entry(current_title)

        return render(request, "encyclopedia/edit.html", {
            "title": current_title,
            "title_page": md_result
        })

    if request.method == "POST":
        edited_text = request.POST.get("edited_entry_text")

        util.save_entry(current_title, edited_text)

        return HttpResponseRedirect(reverse("wiki", kwargs={'title':current_title}))


def random_page(request):
    if request.method == "GET":
        titles = util.list_entries()

        title = random.choice(titles)

        return HttpResponseRedirect(reverse("wiki", kwargs={'title':title}))