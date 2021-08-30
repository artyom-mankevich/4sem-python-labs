import pytest

from store.forms import UserRegisterForm


@pytest.mark.parametrize(
    'username, email, first_name, last_name,'
    ' password1, password2, validity',
    [
        # everything's correct w/o optional fields
        ('billy', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', True),
        # everything's correct w/ optional field
        ('billy', 'billy@gym.com', 'Billy', 'Billyson', 'bossofthegym', 'bossofthegym', True),
        # no 2nd pwd
        ('billy', 'billy@gym.com', '', '', 'bossofthegym', '', False),
        # no 1st pwd
        ('billy', 'billy@gym.com', '', '', '', 'bossofthegym', False),
        # incorrect username
        ('billy^^^', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', False),
        # username too short
        ('b', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', False),
        # username too long
        ('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbilly', 'billy@gym.com', '', '', 'bossofthegym',
         'bossofthegym', False),
        # no username
        ('', 'billy@gym.com', '', '', 'bossofthegym', 'bossofthegym', False),
        # invalid email
        ('billy', 'billygym.com', '', '', 'bossofthegym', 'bossofthegym', False),
        # no email
        ('billy', '', '', '', 'bossofthegym', 'bossofthegym', False),
        # invalid first_name
        ('billy', 'billy@gym.com', 'billy', '', 'bossofthegym', 'bossofthegym', False),
        # invalid last_name
        ('billy', 'billy@gym.com', '', 'billyson', 'bossofthegym', 'bossofthegym', False),
    ]
)
@pytest.mark.django_db
def test_register_form_validation(client, username, email,
                                first_name, last_name,
                                password1, password2, validity):
    form = UserRegisterForm(
        data={
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password1': password1,
            'password2': password2,
        },
    )
    assert form.is_valid() is validity
