from django.test import TestCase

from store.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(category="Poster",
                               size="24\" x 18\"",
                               price="29.99",
                               title="Self-portrait",
                               art_dating="1887",
                               art_id="SK-A-3262",
                               artist="Vincent van Gogh",
                               artist_birth="1853-03-30",
                               artist_death="1890-07-29",
                               artist_nationality="Nederlands",
                               art_description="Vincent moved to Paris in 1886, after hearing from his brother Theo "
                                               "about the new, colourful style of French painting. Wasting no time, "
                                               "he tried it out in several self-portraits. He did this mostly to "
                                               "avoid having to pay for a model. Using rhythmic brushstrokes in "
                                               "striking colours, he portrayed himself here as a fashionably dressed "
                                               "Parisian.")

    # region verbose_name tests
    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_size_label(self):
        product = Product.objects.get(id=1)
        size_label = product._meta.get_field('size').verbose_name
        self.assertEqual(size_label, 'size')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        price_label = product._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')

    def test_title_label(self):
        product = Product.objects.get(id=1)
        title_label = product._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_art_dating_label(self):
        product = Product.objects.get(id=1)
        art_dating_label = product._meta.get_field('art_dating').verbose_name
        self.assertEqual(art_dating_label, 'art dating')

    def test_art_id_label(self):
        product = Product.objects.get(id=1)
        art_id_label = product._meta.get_field('art_id').verbose_name
        self.assertEqual(art_id_label, 'art id')

    def test_artist_label(self):
        product = Product.objects.get(id=1)
        artist_label = product._meta.get_field('artist').verbose_name
        self.assertEqual(artist_label, 'artist')

    def test_artist_birth_label(self):
        product = Product.objects.get(id=1)
        artist_birth_label = product._meta.get_field('artist_birth').verbose_name
        self.assertEqual(artist_birth_label, 'artist birth')

    def test_artist_death_label(self):
        product = Product.objects.get(id=1)
        artist_death_label = product._meta.get_field('artist_death').verbose_name
        self.assertEqual(artist_death_label, 'artist death')

    def test_artist_nationality_label(self):
        product = Product.objects.get(id=1)
        artist_nationality_label = product._meta.get_field('artist_nationality').verbose_name
        self.assertEqual(artist_nationality_label, 'artist nationality')

    def test_art_description_label(self):
        product = Product.objects.get(id=1)
        art_description_label = product._meta.get_field('art_description').verbose_name
        self.assertEqual(art_description_label, 'art description')

    # endregion

    # region max_length tests
    def test_category_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('category').max_length
        self.assertEqual(max_length, 250)

    def test_size_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('size').max_length
        self.assertEqual(max_length, 50)

    def test_title_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_art_dating_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('art_dating').max_length
        self.assertEqual(max_length, 250)

    def test_art_id_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('art_id').max_length
        self.assertEqual(max_length, 50)

    def test_artist_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('artist').max_length
        self.assertEqual(max_length, 250)

    def test_artist_nationality_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('artist_nationality').max_length
        self.assertEqual(max_length, 50)

    def test_art_description_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('art_description').max_length
        self.assertEqual(max_length, 1000)

    # endregion

    def test_to_string(self):
        product = Product.objects.get(id=1)
        expected_str = f'{product.id} {product.category}' \
                       f' {product.size} {product.price}' \
                       f' {product.title} {product.art_dating}' \
                       f' {product.art_id} {product.artist}'
        self.assertEqual(str(product), expected_str)
