from django.test import SimpleTestCase


from .calc import add, subtract


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = subtract(6, 5)

        self.assertEqual(res, 1)


# docker-compose run --rm app sh -c "python manage.py test"
