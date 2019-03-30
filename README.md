# py-glo-board

<p align="center">
    <img align="center" src="https://cdn.worldvectorlogo.com/logos/gitkraken.svg" width="50%" height="50%" title="Glo Boards">
</p>

>A python library to help interact with GitKraken [Glo Boards API](https://support.gitkraken.com/developers/api/)
<br>

## Supported Endpoints & Features

**API Endpoints:**
>This package supports the following v1 [Glo Boards API endpoints](https://gloapi.gitkraken.com/v1/docs/)

**Boards**

- [x] Create Board
- [x] Edit Board
- [x] Delete Board
- [x] Get Boards
- [x] Get Boards by ID

**Columns**
- [x] Create column
- [x] Edit column
- [x] Delete column

**Cards**
- [x] Create Card
- [x] Edit Card
- [x] Delete Card
- [x] Get Cards
- [x] Get Card By ID
- [x] Get Cards By Column ID

**Attachments**
- [ ] Create Attachment
- [ ] Get Attachments

**Comments**
- [ ] Create Comment
- [ ] Edit Comment
- [ ] Delete Comment
- [ ] Get Comments By Card ID

**User**
- [ ] Get User

## Installing
Until is not uploaded to pypi, it's necessary to install using pip and this repository.  
```bash
pip install https://github.com/dpeite/py-glo-board
```

## Example
```python
from py_glo_boards_api import GloBoard, types

globoard = GloBoard('<YOUR_PAT_TOKEN_HERE>')

# List all boards available (Only gets the id and the name of the board)
globoard.get_boards()

# Or select the fields you need, with the options available in the Glo api
fields=['archived_columns', 'archived_date', 'columns', 'created_by', 'created_date', 'invited_members', 'labels', 'members', 'name']
boards = globoard.get_boards(fields, per_page=3)

# Get card
globoard.get_card('<BOARD_ID>', 'CARD_ID').to_dict()

```

## FAQ
Please refer to [Git Kraken Documentation](https://support.gitkraken.com/developers/overview/) for any
further reading.
## License

[MIT]: https://opensource.org/licenses/MIT

The source code for py-glo-board is released under the [MIT License][MIT].
