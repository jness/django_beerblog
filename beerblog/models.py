from django.db import models


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
    website = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Winery(models.Model):
    """A list of wineries"""

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Beer(models.Model):
    """A Beer Object containing everything we
    need to know about our beer"""

    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery)
    created = models.DateTimeField(auto_now_add=True)
    beer_type = models.ForeignKey(BeerType)
    alcohol_by_volume = models.FloatField()
    image = models.ImageField(upload_to='images/')

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

    def __unicode__(self):
        return self.name


class Wine(models.Model):
    """A Wine Object containing everything we
    need to know about our wine"""

    name = models.CharField(max_length=255)
    winery = models.ForeignKey(Winery)
    created = models.DateTimeField(auto_now_add=True)
    wine_type = models.ForeignKey(WineType)
    alcohol_by_volume = models.FloatField()
    image = models.ImageField(upload_to='images/')

    comments = models.TextField(null=True, blank=True)

    # Wine Rating and Score Inputs
    appearance_score = models.ForeignKey(Rating,
                                         related_name='wine_appearance')
    appearance = models.TextField()

    smell_score = models.ForeignKey(Rating, related_name='wine_smell')
    smell = models.TextField()

    taste_score = models.ForeignKey(Rating, related_name='wine_taste')
    taste = models.TextField()

    mouthfeel_score = models.ForeignKey(Rating, related_name='wine_mouthfeel')
    mouthfeel = models.TextField()

    overall_score = models.ForeignKey(Rating, related_name='wine_overall')
    overall = models.TextField()

    def __unicode__(self):
        return self.name
