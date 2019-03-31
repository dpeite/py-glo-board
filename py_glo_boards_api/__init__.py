from . import api, types

class GloBoard:
    def __init__(self, token):
        self.token = token

    # Boards
    def get_boards(self, fields=None, archived=False, page=1, per_page=50, sort='asc'):
        boards = api.get_boards(self.token, fields, archived, page, per_page, sort)
        ret = []
        for board in boards:
            ret.append(types.Board.de_json(board))
        return ret

    def create_board(self, board_name):
        result = api.create_board(self.token, board_name)
        #TODO result is a board object, parse result
        return result

    def get_board(self, board_id, fields=None):
        board = api.get_board(self.token, board_id, fields)
        return types.Board.de_json(board)

    def edit_board(self, board_id, board_name):
        board = api.edit_board(self.token, board_id, board_name)
        return types.Board.de_json(board)

    def delete_board(self, board_id):
        result = api.delete_board(self.token, board_id)
        return result

    # Columns
    def create_column(self, board_id, column_name, position=None):
        column = api.create_column(self.token, board_id, column_name, position)
        return types.Column.de_json(column)

    def edit_column(self, board_id, column_id, column_name, position=None):
        column = api.edit_column(self.token, board_id, column_id, column_name, position)
        return types.Column.de_json(column)

    def delete_column(self, board_id, column_id):
        result = api.delete_column(self.token, board_id, column_id)
        return result

    # Cards
    def get_cards(self, board_id, fields=None, archived=False, page=1, per_page=50, sort='asc'):
        cards = api.get_cards(self.token, board_id, fields, archived, page, per_page, sort)
        ret = []
        for card in cards:
            ret.append(types.Card.de_json(card))
        return ret

    def get_cards_column(self, board_id, column_id, fields=None, archived=False, page=1, per_page=50, sort='asc'):
        cards = api.get_cards_column(self.token, board_id, column_id, fields, archived, page, per_page, sort)
        ret = []
        for card in cards:
            ret.append(types.Card.de_json(card))
        return ret

    def create_card(self, board_id, column_id, card_name, position=None, description=None,
                    assignees=None, labels=None, due_date=None):
        #TODO Test the optional parameters
        card = api.create_card(self.token, board_id, column_id, card_name, position, description, assignees, labels, due_date)
        return types.Card.de_json(card)

    def create_card_batch(self, board_id, batch):
        cards = api.create_card_batch(self.token, board_id, batch)
        ret = []
        for card in cards:
            ret.append(types.Card.de_json(card))
        return ret

    def get_card(self, board_id, card_id, fields=None):
        card = api.get_card(self.token, board_id, card_id, fields)
        return types.Card.de_json(card)

    def edit_card(self, board_id, card_id, card_name, position=None, description=None,
                    assignees=None, labels=None, due_date=None):
        #TODO Test the optional parameters
        card = api.edit_card(self.token, board_id, card_id, card_name, position, description, assignees, labels, due_date)
        return types.Card.de_json(card)

    def delete_card(self, board_id, card_id):
        result = api.delete_card(self.token, board_id, card_id)
        return result

    # Labels
    def create_label(self, board_id, label):
        label = api.create_label(self.token, board_id, label)
        return types.Label.de_json(label)

    def edit_label(self, board_id, label_id, label):
        label = api.edit_label(self.token, board_id, label_id, label)
        return types.Label.de_json(label)

    def delete_label(self, board_id, label_id):
        result = api.delete_label(self.token, board_id, label_id)
        return result

    # Attachments
    def get_attachments(self, board_id, card_id, fields=None, archived=False, page=1, per_page=50, sort='asc'):
        attachments = api.get_attachments(self.token, board_id, card_id, fields, archived, page, per_page, sort)
        ret = []
        for attachment in attachments:
            ret.append(types.Attachment.de_json(attachment))
        return ret

    def create_attachment(self, board_id, card_id, attachment):
        attachment = api.create_attachment(self.token, board_id, card_id, attachment)
        return types.Attachment.de_json(attachment)

    # Comments
    def get_comments(self, board_id, card_id, fields=None, archived=False, page=1, per_page=50, sort='asc'):
        comments = api.get_comments(self.token, board_id, card_id, fields, archived, page, per_page, sort)
        ret = []
        for comment in comments:
            ret.append(types.Comment.de_json(comment))
        return ret

    def create_comment(self, board_id, card_id, comment):
        comment = api.create_comment(self.token, board_id, card_id, comment)
        return types.Comment.de_json(comment)

    def edit_comment(self, board_id, card_id, comment_id, comment):
        comment = api.edit_comment(self.token, board_id, card_id, comment_id, comment)
        return types.Comment.de_json(comment)

    def delete_comment(self, board_id, card_id, comment_id):
        result = api.delete_comment(self.token, board_id, card_id, comment_id)
        return result

    # User
    def get_user(self, fields=None):
        user = api.get_user(self.token, fields)
        return types.User.de_json(user)