from datetime import datetime


class Board:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        name = obj.get('name')
        created_by = obj.get('created_by')

        archived_columns = obj.get('archived_columns')
        if archived_columns:
            archived_columns = []
            for archived_column in obj.get('archived_columns'):
                archived_columns.append(Column.de_json(archived_column))

        archived_date = obj.get('archived_date')
        if archived_date:
            archived_date = datetime.strptime(archived_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        columns = obj.get('columns')
        if columns:
            columns = []
            for column in obj.get('columns'):
                columns.append(Column.de_json(column))

        created_date = obj.get('created_date')
        if created_date:
            created_date = datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        invited_members = obj.get('invited_members')
        if invited_members:
            invited_members = []
            for invited_member in obj.get('invited_members'):
                invited_members.append(Label.de_json(invited_member))

        labels = obj.get('labels')
        if labels:
            labels = []
            for label in obj.get('labels'):
                labels.append(Label.de_json(label))

        members = obj.get('members')
        if members:
            members = []
            for member in obj.get('members'):
                members.append(Label.de_json(member))

        return cls(id, name, archived_columns, archived_date, columns, created_by, created_date, invited_members, labels, members)

    def __init__(self, id, name, archived_columns, archived_date, columns, created_by, created_date, invited_members, labels, members):
        self.id = id
        self.name = name
        self.archived_columns = archived_columns
        self.archived_date = archived_date
        self.columns = columns
        self.created_by = created_by
        self.created_date = created_date
        self.invited_members = invited_members
        self.labels = labels
        self.members = members

    def to_dic(self):
        return {
            'id': self.id,
            'name': self.name,
            'archived_columns': [archived_column.to_dict() for archived_column in self.archived_columns] if self.archived_columns else None,
            'archived_date': self.archived_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.archived_date else None,
            'columns': [column.to_dict() for column in self.columns] if self.columns else None,
            'created_by': self.created_by,
            'created_date': self.created_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.created_date else None,
            'invited_members': [invited_member.to_dict() for invited_member in self.invited_members] if self.invited_members else None,
            'labels': [label.to_dict() for label in self.labels] if self.labels else None,
            'members': [member.to_dict() for member in self.members] if self.members else None
        }

class BoardMember:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        role = obj.get('role')
        username = obj.get('username')
        return cls(id, role, username)

    def __init__(self, id, role, username):
        self.id = id
        self.role = role
        self.username = username

    def to_dict(self):
        return {
            'id': self.id,
            'role': self.role,
            'username': self.username
        }


class Column:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        name = obj.get('name')
        position = obj.get('position')
        archived_date = obj.get('archived_date')
        if archived_date:
            archived_date = datetime.strptime(archived_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        created_date = obj.get('created_date')
        if created_date:
            created_date = datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        created_by = obj.get('created_by')
        return cls(id, name, position, archived_date, created_date, created_by)

    def __init__(self, id, name, position, archived_date, created_date, created_by):
        self.id = id
        self.name = name
        self.position = position
        self.archived_date = archived_date
        self.created_date = created_date
        self.created_by = created_by

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'archived_date': self.archived_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.archived_date else None,
            'created_date': self.created_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.created_date else None,
            'created_by': self.created_by,
        }

class Label:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        name = obj.get('name')
        color = obj.get('color')
        created_date = obj.get('created_date')
        if created_date:
            created_date = datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        created_by = obj.get('created_by')
        return cls(name, color, created_date, created_by, id)

    def __init__(self, name, color, created_date=None, created_by=None, id=None):
        self.id = id
        self.name = name
        self.color = color
        self.created_date = created_date
        self.created_by = created_by

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'created_date': self.created_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.created_date else None,
            'created_by': self.created_by,
        }


class Card:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        name = obj.get('name')
        position = obj.get('position')
        description = obj.get('description')
        board_id = obj.get('board_id')
        column_id = obj.get('column_id')

        created_date = obj.get('created_date')
        if created_date:
            created_date = datetime.strptime(created_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        updated_date = obj.get('updated_date')
        if updated_date:
            updated_date = datetime.strptime(updated_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        archived_date = obj.get('archived_date')
        if archived_date:
            archived_date = datetime.strptime(archived_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        assignees = obj.get('assignees')
        if assignees:
            assignees = []
            for assignee in obj.get('assignees'):
                assignees.append(Label.de_json(assignee))

        labels = obj.get('labels')
        if labels:
            labels = []
            for label in obj.get('labels'):
                labels.append(Label.de_json(label))

        due_date = obj.get('due_date')
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        comment_count = obj.get('comment_count')
        attachment_count = obj.get('attachment_count')
        completed_task_count = obj.get('completed_task_count')
        total_task_count = obj.get('total_task_count')
        created_by = obj.get('created_by')

        return cls(id, name, position, description, board_id, column_id, created_date, updated_date, archived_date,
                   assignees, labels, due_date, comment_count, attachment_count, completed_task_count,
                   total_task_count, created_by)

    def __init__(self, id, name, position, description, board_id, column_id, created_date, updated_date, archived_date,
                 assignees, labels, due_date, comment_count, attachment_count, completed_task_count, total_task_count,
                 created_by):
        self.id = id
        self.name = name
        self.position = position
        self.description = description
        self.board_id = board_id
        self.column_id = column_id
        self.created_date = created_date
        self.updated_date = updated_date
        self.archived_date = archived_date
        self.assignees = assignees
        self.labels = labels
        self.due_date = due_date
        self.comment_count = comment_count
        self.attachment_count = attachment_count
        self.completed_task_count = completed_task_count
        self.total_task_count = total_task_count
        self.created_by = created_by

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'description': self.description,
            'board_id': self.board_id,
            'column_id': self.column_id,
            'created_date': self.created_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.created_date else None,
            'updated_date': self.updated_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.updated_date else None,
            'archived_date': self.archived_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.archived_date else None,
            'assignees': [assignee.to_dict() for assignee in self.assignees] if self.assignees else None,
            'labels': [label.to_dict() for label in self.labels] if self.labels else None,
            'due_date': self.due_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ") if self.due_date else None,
            'comment_count': self.comment_count,
            'attachment_count': self.attachment_count,
            'completed_task_count': self.completed_task_count,
            'total_task_count': self.total_task_count,
            'created_by': self.created_by,
        }


class PartialUser:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        return cls(id)

    def __init__(self, id):
        self.id = id

    def to_dict(self):
        return {
            'id': self.id
        }


class PartialLabel:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        name = obj.get('name')
        return cls(id, name)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Attachment:
    @classmethod
    def de_json(cls, obj):
        id = obj.get('id')
        filename = obj.get('filename')
        mime_type = obj.get('mime_type')
        return cls(id, filename, mime_type)

    def __init__(self, id, filename, mime_type):
        self.id = id
        self.filename = filename
        self.mime_type = mime_type

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'mime_type': self.mime_type
        }
