from datetime import datetime
from uuid import uuid4

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from security import get_password_hash
from adapter.database.db import get_db


def populate():
    try:
        session = next(get_db())

        user_1_id = uuid4()
        user_2_id = uuid4()
        user_3_id = uuid4()
        user_4_id = uuid4()

        session.execute(
            text(
                f'''
                INSERT INTO users (id, username, nome, email, cpf, hashed_password, is_active, is_deleted, created_at, updated_at)
                VALUES 
                    ('{user_1_id}', 'joao', 'João', 'joao@email.com', '11122233344', '{get_password_hash('password')}', true, false, '{datetime.utcnow()}', null),
                    ('{user_2_id}', 'victor', 'Victor', 'victor@email.com', '22233344455', '{get_password_hash('password')}', true, false, '{datetime.utcnow()}', null),
                    ('{user_3_id}', 'tais', 'Tais', 'tais@email.com', '33344455566', '{get_password_hash('password')}', true, false, '{datetime.utcnow()}', null),
                    ('{user_4_id}', 'augusto', 'Augusto', 'augusto@email.com', '44455566677', '{get_password_hash('password')}', true, false, '{datetime.utcnow()}', null)
                '''
            )
        )
        session.commit()

        category_1_id = uuid4()
        category_2_id = uuid4()
        category_3_id = uuid4()

        session.execute(
            text(
                f'''
                    INSERT INTO categories (id, nome, is_active, is_deleted, created_at, updated_at, created_by, updated_by)
                    VALUES 
                        ('{category_1_id}', 'Lanches', true, false, '{datetime.utcnow()}', null, '{user_1_id}', null),
                        ('{category_2_id}', 'Sobremesas', true, false, '{datetime.utcnow()}', null, '{user_2_id}', null),
                        ('{category_3_id}', 'Refrigerantes', true, false, '{datetime.utcnow()}', null, '{user_3_id}', null)
                    '''
            )
        )
        session.commit()

        product_1_id = uuid4()
        product_2_id = uuid4()
        product_3_id = uuid4()
        product_4_id = uuid4()
        product_5_id = uuid4()
        product_6_id = uuid4()
        product_7_id = uuid4()

        session.execute(
            text(
                f'''
                        INSERT INTO products (id, nome, is_active, is_deleted, created_at, updated_at, category_id, created_by, updated_by)
                        VALUES 
                            ('{product_1_id}', 'Whopper', true, false, '{datetime.utcnow()}', null, '{category_1_id}', '{user_1_id}', null),
                            ('{product_2_id}', 'BigMc', true, false, '{datetime.utcnow()}', null, '{category_1_id}', '{user_2_id}', null),
                            ('{product_3_id}', 'Cheddar', true, false, '{datetime.utcnow()}', null, '{category_1_id}', '{user_3_id}', null),
                            ('{product_4_id}', 'Coca-Cola', true, false, '{datetime.utcnow()}', null, '{category_3_id}', '{user_4_id}', null),
                            ('{product_5_id}', 'Guaraná', true, false, '{datetime.utcnow()}', null, '{category_3_id}', '{user_1_id}', null),
                            ('{product_6_id}', 'Casquinha', true, false, '{datetime.utcnow()}', null, '{category_2_id}', '{user_2_id}', null),
                            ('{product_7_id}', 'Torta de maçã', true, false, '{datetime.utcnow()}', null, '{category_2_id}', '{user_3_id}', null)
                        '''
            )
        )
        session.commit()

        session.close()

    except IntegrityError:
        pass
