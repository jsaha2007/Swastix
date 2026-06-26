"""
Alembic Migration Setup Guide

This guide helps you set up database migrations with Alembic for version control
of your database schema.

Note: For MVP, direct table creation with init_db.py is sufficient.
Use Alembic for production and team development environments.
"""

# ============================================================================
# SETUP INSTRUCTIONS
# ============================================================================

"""
1. Initialize Alembic (one-time setup):

   alembic init alembic

2. Update alembic/env.py:

   Replace the import section with:

   ```python
   from sqlalchemy import engine_from_config, pool
   from alembic import context
   from config import DATABASE_URL
   from database import Base
   from models import *  # Import all models

   # ... rest of the file
   ```

3. Update alembic.ini:

   Change:
   sqlalchemy.url = postgresql://username:password@localhost:5432/swastix_db

4. Create initial migration:

   alembic revision --autogenerate -m "Initial migration"

5. Apply migration:

   alembic upgrade head

6. View migration history:

   alembic history

7. Downgrade to previous version:

   alembic downgrade -1
"""

# ============================================================================
# MIGRATION COMMANDS
# ============================================================================

"""
Common Alembic Commands:

# Create a new migration script
alembic revision -m "Add new column to doctors"

# Auto-generate migration (detects model changes)
alembic revision --autogenerate -m "Add consultation_type to appointments"

# Apply latest migrations
alembic upgrade head

# Apply specific migration
alembic upgrade ae1027a6acf

# Downgrade one version
alembic downgrade -1

# Downgrade to specific version
alembic downgrade 1975ea83175

# View all migrations
alembic history

# Current database version
alembic current

# View migration details
alembic show ae1027a6acf
"""

# ============================================================================
# SAMPLE MIGRATION FILE
# ============================================================================

"""
This is what an auto-generated migration looks like:

'''
\"\"\"Initial migration

Revision ID: 1975ea83175
Revises: 
Create Date: 2024-01-15 10:30:00.000000

\"\"\"
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '1975ea83175'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create all tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=False),
        sa.Column('role', sa.Enum('patient', 'doctor', 'admin', name='roleenum'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('is_verified', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=True)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    op.create_index(op.f('ix_users_is_active'), 'users', ['is_active'], unique=False)
    # ... more tables


def downgrade() -> None:
    # Drop all tables in reverse order
    op.drop_index(op.f('ix_users_is_active'), table_name='users')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_phone'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ... more tables
'''
"""

# ============================================================================
# FOR MVP: KEEP IT SIMPLE
# ============================================================================

"""
For the MVP phase, you can skip Alembic and use init_db.py:

# Initialize database (creates all tables)
python init_db.py

# Drop database and recreate (if needed)
python init_db.py drop

Benefits:
- Simple and fast
- Easy to understand
- No migration files to manage
- Perfect for development and MVP

When to Use Alembic:
- Production deployments
- Multiple developers
- Schema version tracking
- Automated CI/CD deployments
- Database rollback requirements
"""

# ============================================================================
# PRODUCTION MIGRATION STRATEGY
# ============================================================================

"""
For production, implement this strategy:

1. Development:
   - Use init_db.py for quick setup
   - Test all models locally

2. Before Deployment:
   - Auto-generate Alembic migration: alembic revision --autogenerate
   - Review the migration file
   - Test migration on backup database
   - Commit migration to version control

3. Deployment:
   - Run migration: alembic upgrade head
   - Verify data integrity
   - Keep migration history in git

4. Rollback (if needed):
   - Run: alembic downgrade <previous_version>
   - Fix the issue
   - Create new migration
"""

if __name__ == "__main__":
    print("""
    ========================================
    Alembic Migration Guide
    ========================================

    For MVP: Use init_db.py directly
    Command: python init_db.py

    For Production: Use Alembic
    Setup: Follow instructions in comments above

    Questions? Check: DATABASE_SCHEMA.md
    ========================================
    """)
