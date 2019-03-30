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

    def create_card_batch(self):
        raise NotImplementedError

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

    def create_label(self, board_id, label):
        label = api.create_label(self.token, board_id, label)
        return types.Label.de_json(label)

    def edit_label(self, board_id, label_id, label):
        label = api.edit_label(self.token, board_id, label_id, label)
        return types.Label.de_json(label)

    def delete_label(self, board_id, label_id):
        result = api.delete_label(self.token, board_id, label_id)
        return result

    # def get_attachments(self, board_id, card_id, fields=None, archived=False, page=1, per_page=50, sort='asc'):
    #     attachments = api.get_attachments(board_id, card_id, fields, archived, page, per_page, sort)
    #     ret = []
    #     for attachment in attachments:
    #         ret.append(types.Attachment.de_json(attachment))
    #     return ret