from django.http import HttpResponse, HttpResponseNotFound
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

from bscloud.models import Board

import json
import random


def start_page(request):
    template = get_template('main.html')

    context = Context({
        # 'show_full_logo': True,
        # 'show_navigation_bar': True,
        # 'navigation_bar_items': navigation_bar.items,
        # 'show_blog': True,
        # 'is_published': True,
        # 'show_blog_on_header': True,
        # 'blog_posts': last_posts,
    })

    html = template.render(context)

    return HttpResponse(html)


def board_reg(request):
    hash_str = '%032x' % random.getrandbits(128)
    board = Board.create(hash_str)
    board.save()

    answer = json.dumps({'board_id': hash_str})
    return HttpResponse(answer)