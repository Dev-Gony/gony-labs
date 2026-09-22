"""initial question and answer tables

Revision ID: 20260922_01
Revises:
Create Date: 2026-09-22
"""

from alembic import op
import sqlalchemy as sa


revision = "20260922_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("questions", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("topic", sa.String(length=100), nullable=False), sa.Column("prompt", sa.Text(), nullable=False))
    op.create_table("answers", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("question_id", sa.Integer(), sa.ForeignKey("questions.id"), nullable=False), sa.Column("content", sa.Text(), nullable=False), sa.Column("created_at", sa.DateTime(), nullable=False))
    op.create_index("ix_answers_question_id", "answers", ["question_id"])


def downgrade() -> None:
    op.drop_index("ix_answers_question_id", table_name="answers")
    op.drop_table("answers")
    op.drop_table("questions")
