from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from django.template.defaultfilters import slugify

from os import symlink, remove


class BeerType(models.Model):
    """The different beer types"""

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class WineType(models.Model):
    """The different wine types"""

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    """Allowed Ratings for our beer categories"""

    class Meta:
        ordering = ['value']

    value = models.FloatField()

    def __unicode__(self):
        return str(self.value)


class Brewery(models.Model):
    """A list of breweries"""

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Winery(models.Model):
    """A list of wineries"""

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Beer(models.Model):
    """A Beer Object containing everything we
    need to know about our beer"""

    class Meta:
        ordering = ['name']

    def get_image_path(self, filename):
        extension = filename.split('.')[-1]
        return 'images/uploads/%s.%s' % (slugify(self.name), extension)

    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery)
    created = models.DateTimeField(auto_now_add=True)
    beer_type = models.ForeignKey(BeerType)
    alcohol_by_volume = models.FloatField()
    image = ImageWithThumbsField(upload_to=get_image_path,
                                 sizes=((200, 200), (600, 800)),
                                 null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    # Beer Rating and Score Inputs
    appearance_score = models.ForeignKey(Rating,
                                         related_name='beer_appearance')
    appearance = models.TextField()

    smell_score = models.ForeignKey(Rating, related_name='beer_smell')
    smell = models.TextField()

    taste_score = models.ForeignKey(Rating, related_name='beer_taste')
    taste = models.TextField()

    mouthfeel_score = models.ForeignKey(Rating, related_name='beer_mouthfeel')
    mouthfeel = models.TextField()

    overall_score = models.ForeignKey(Rating, related_name='beer_overall')
    overall = models.TextField()

    @property
    def rating(self):
        """Sum up all our scores and get our average rating"""
        return sum([self.appearance_score.value, self.smell_score.value,
                    self.taste_score.value, self.mouthfeel_score.value,
                    self.overall_score.value]) / 5

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Beer, self).save(*args, **kwargs)

        if self.image:
            extension = self.image.path.split('.')[-1]
            path = '/'.join(self.image.path.split('/')[:-1])

            remove('%s/%s.%s' % (path, slugify(self.name), extension))

            symlink('%s/%s.600x800.%s' % (path, slugify(self.name), extension),
                    '%s/%s.%s' % (path, slugify(self.name), extension))


class Wine(models.Model):
    """A Wine Object containing everything we
    need to know about our wine"""

    class Meta:
        ordering = ['name']

    def get_image_path(self, filename):
        extension = filename.split('.')[-1]
        return 'images/uploads/%s.%s' % (slugify(self.name), extension)

    name = models.CharField(max_length=255)
    winery = models.ForeignKey(Winery)
    created = models.DateTimeField(auto_now_add=True)
    wine_type = models.ForeignKey(WineType)
    alcohol_by_volume = models.FloatField()
    image = ImageWithThumbsField(upload_to=get_image_path,
                                 sizes=((200, 200), (600, 800)),
                                 null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    # Wine Rating and Score Inputs
    sight_score = models.ForeignKey(Rating,
                                         related_name='wine_sight')
    sight = models.TextField()

    smell_score = models.ForeignKey(Rating, related_name='wine_smell')
    smell = models.TextField()

    swirl_score = models.ForeignKey(Rating, related_name='wine_swirl')
    swirl = models.TextField()

    sip_score = models.ForeignKey(Rating, related_name='wine_sip')
    sip = models.TextField()

    savor_score = models.ForeignKey(Rating, related_name='wine_savor')
    savor = models.TextField()

    @property
    def rating(self):
        """Sum up all our scores and get our average rating"""
        return sum([self.sight_score.value, self.smell_score.value,
                    self.swirl_score.value, self.sip_score.value,
                    self.savor_score.value]) / 5

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Wine, self).save(*args, **kwargs)

        if self.image:
            extension = self.image.path.split('.')[-1]
            path = '/'.join(self.image.path.split('/')[:-1])

            remove('%s/%s.%s' % (path, slugify(self.name), extension))

            symlink('%s/%s.600x800.%s' % (path, slugify(self.name), extension),
                    '%s/%s.%s' % (path, slugify(self.name), extension))
