"""create ckanext-publikasi table

Revision ID: 0762c8ef9ad1
Revises: 
Create Date: 2025-01-13 15:45:03.999832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0762c8ef9ad1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    engine = op.get_bind()
    inspector = sa.inspect(engine)
    tables = inspector.get_table_names()

    if "ckanext_publikasi" not in tables:
        op.create_table(
            "ckanext_publikasi",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("unique_id", sa.UnicodeText, unique=True), # UUID dan Unique
            sa.Column("title", sa.UnicodeText),
            sa.Column("desciption", sa.UnicodeText, default=""),
            sa.Column("author", sa.UnicodeText, default=""),
            sa.Column("file_path", sa.UnicodeText, default=""),
            sa.Column("user_own", sa.UnicodeText, default=""), # User yang membuat record
            sa.Column("cover_image", sa.UnicodeText, nullable=True), # Cover image text / blob file
            sa.Column("meta_catalog_number", sa.String(50), nullable=True), # JSON metadata berkas
            sa.Column("meta_publication_number", sa.String(50), nullable=True), # JSON metadata berkas
            sa.Column("meta_isbn_issn", sa.String(50), nullable=True), # JSON metadata berkas
            sa.Column("meta_release_freqency", sa.String(50), nullable=True), # JSON metadata berkas
            sa.Column("meta_release_date", sa.DateTime), # JSON metadata berkas
            sa.Column("meta_language", sa.String(50), nullable=True), # JSON metadata berkas
            sa.Column("meta_file_size", sa.BigInteger, nullable=True), # JSON metadata berkas
            sa.Column("created", sa.DateTime),
            sa.Column("modified", sa.DateTime)
        )


def downgrade():
    op.drop_table("ckanext_publikasi")
