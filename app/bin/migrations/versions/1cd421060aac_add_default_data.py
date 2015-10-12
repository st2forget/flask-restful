"""Add default data

Revision ID: 1cd421060aac
Revises: f653df56bb5
Create Date: 2015-10-12 11:34:38.518803

"""

# revision identifiers, used by Alembic.
revision = '1cd421060aac'
down_revision = 'f653df56bb5'

from alembic import op
import string, random
from sqlalchemy.sql import table, column
from sqlalchemy import String, Text, Boolean

def upgrade():

    ### commands auto generated by Alembic - please adjust! ###
    client_table = table('client',
                         column('client_id', String(40)),
                         column('client_secret', String(55)),
                         column('_redirect_uris', Text),
                         column('is_confidential', Boolean)
                         )

    op.bulk_insert(client_table,
                   [
                       {
                           'client_id': ''.join(random.choice(string.ascii_uppercase) for i in range(40)),
                           'client_secret': ''.join(random.choice(string.ascii_uppercase) for i in range(55)),
                           '_redirect_uris': 'application/authorized',
                           'is_confidential': 1
                       }
                   ])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    ### commands auto generated by Alembic - please adjust! ###
    client_table = table('client',
                         column('client_id', String(40)),
                         column('client_secret', String(55)))


    op.execute(client_table.delete())
    ### end Alembic commands ###