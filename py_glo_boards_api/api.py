import requests
import json

API_URL = "https://gloapi.gitkraken.com/v1/glo/{0}"
CONNECT_TIMEOUT = 3.5


def _make_request(token, method_name, method='get', params={}, json_params=None, files=None):
    payload = {'access_token': token}
    payload.update(params)
    result = requests.request(method, API_URL.format(method_name), params=payload, json=json_params, files=files, timeout=CONNECT_TIMEOUT)
    if result.status_code == 204:
        return True
    if result.status_code == 400 or result.status_code == 404:
        raise GloException(result.text)
    return result.json()


# Boards
def get_boards(token, fields, archived, page, per_page, sort):
    method_name = 'boards'
    params = {
        'fields': fields,
        'archived': archived,
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    return _make_request(token, method_name, params=params)


def create_board(token, board_name):
    method_name = 'boards'
    data = {'name': board_name}
    return _make_request(token, method_name, 'post', json_params=data)


def get_board(token, board_id, fields):
    method_name = 'boards/{}'.format(board_id)
    params = {
        'fields': fields
    }
    return _make_request(token, method_name, params=params)


def edit_board(token, board_id, board_name):
    method_name = 'boards/{}'.format(board_id)
    data = {'name': board_name}
    return _make_request(token, method_name, 'post', json_params=data)


def delete_board(token, board_id):
    method_name = 'boards/{}'.format(board_id)
    return _make_request(token, method_name, 'delete')


# Columns
def create_column(token, board_id, column_name, position=None):
    method_name = 'boards/{}/columns'.format(board_id)
    data = {'name': column_name}
    if position:
        data['position'] = position
    return _make_request(token, method_name, 'post', json_params=data)


def edit_column(token, board_id, column_id, column_name, position=None):
    method_name = 'boards/{}/columns/{}'.format(board_id, column_id)
    data = {'name': column_name}
    if position:
        data['position'] = position
    return _make_request(token, method_name, 'post', json_params=data)


def delete_column(token, board_id, column_id):
    method_name = 'boards/{}/columns/{}'.format(board_id, column_id)
    return _make_request(token, method_name, 'delete')


# Cards
def get_cards(token, board_id, fields, archived, page, per_page, sort):
    method_name = 'boards/{}/cards'.format(board_id)
    params = {
        'fields': fields,
        'archived': archived,
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    return _make_request(token, method_name, 'get', params=params)


def get_cards_column(token, board_id, column_id, fields, archived, page, per_page, sort):
    method_name = 'boards/{}/columns/{}/cards'.format(board_id, column_id)
    params = {
        'fields': fields,
        'archived': archived,
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    return _make_request(token, method_name, 'get', params=params)


def create_card(token, board_id, column_id, card_name, position=None, description=None,
                assignees=None, labels=None, due_date=None):
    method_name = 'boards/{}/cards'.format(board_id)
    data = {'name': card_name,
            'column_id': column_id}
    if position:
        data['position'] = position
    if description:
        data['description'] = description
    if assignees:
        data['assignees'] = assignees
    if labels:
        data['labels'] = labels
    if due_date:
        data['due_date'] = due_date

    return _make_request(token, method_name, 'post', json_params=data)


def create_card_batch(token, board_id, batch):
    method_name = 'boards/{}/cards/batch'.format(board_id)
    return _make_request(token, method_name, 'post', json_params=batch)


def get_card(token, board_id, card_id, fields):
    method_name = 'boards/{}/cards/{}'.format(board_id, card_id)
    params = {
        'fields': fields
    }
    return _make_request(token, method_name, 'get', params=params)


def edit_card(token, board_id, card_id, card_name, column_id=None, position=None, description=None,
              assignees=None, labels=None, due_date=None):
    method_name = 'boards/{}/cards/{}'.format(board_id, card_id)
    data = {'name': card_name}
    if position:
        data['position'] = position
    if description:
        data['description'] = description
    if assignees:
        data['assignees'] = assignees
    if labels:
        data['labels'] = labels
    if due_date:
        data['due_date'] = due_date
    if column_id:
        data['column_id'] = column_id

    return _make_request(token, method_name, 'post', json_params=data)


def delete_card(token, board_id, card_id):
    method_name = 'boards/{}/cards/{}'.format(board_id, card_id)
    return _make_request(token, method_name, 'delete')

# Labels
def create_label(token, board_id, label):
    method_name = 'boards/{}/labels/'.format(board_id)
    return _make_request(token, method_name, 'post', json_params=label.to_dict())


def edit_label(token, board_id, label_id, label):
    method_name = 'boards/{}/labels/{}'.format(board_id, label_id)
    return _make_request(token, method_name, 'post', json_params=label.to_dict())


def delete_label(token, board_id, label_id):
    method_name = 'boards/{}/labels/{}'.format(board_id, label_id)
    return _make_request(token, method_name, 'delete')


# Attachments
def get_attachments(token, board_id, card_id, fields, archived, page, per_page, sort):
    method_name = 'boards/{}/cards/{}/attachments'.format(board_id, card_id)
    params = {
        'fields': fields,
        'archived': archived,
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    return _make_request(token, method_name, 'get', params=params)


def create_attachment(token, board_id, card_id, attachment):
    method_name = 'boards/{}/cards/{}/attachments'.format(board_id, card_id)
    files = {'filename': attachment}
    return _make_request(token, method_name, 'post', files=files)


# Comments
def get_comments(token, board_id, card_id, fields, archived, page, per_page, sort):
    method_name = 'boards/{}/cards/{}/comments'.format(board_id, card_id)
    params = {
        'fields': fields,
        'archived': archived,
        'page': page,
        'per_page': per_page,
        'sort': sort
    }
    return _make_request(token, method_name, 'get', params=params)


def create_comment(token, board_id, card_id, comment):
    method_name = 'boards/{}/cards/{}/comments'.format(board_id, card_id)
    data = {'text': comment}
    return _make_request(token, method_name, 'post', json_params=data)


def edit_comment(token, board_id, card_id, comment_id, comment):
    method_name = 'boards/{}/cards/{}/comments/{}'.format(board_id, card_id, comment_id)
    data = {'text': comment}
    return _make_request(token, method_name, 'post', json_params=data)


def delete_comment(token, board_id, card_id, comment_id):
    method_name = 'boards/{}/cards/{}/comments/{}'.format(board_id, card_id, comment_id)
    return _make_request(token, method_name, 'delete')


# User
def get_user(token, fields):
    method_name = 'user'.format()
    params = {
        'fields': fields
    }
    return _make_request(token, method_name, 'get', params=params)


class GloException(Exception):
    pass
