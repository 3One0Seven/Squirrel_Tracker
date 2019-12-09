from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    X = models.FloatField(
        help_text=_('Longitude'),
        null=True,
    )
    
    Y = models.FloatField(
        help_text=_('Latitude'),
        null=True,
    )

    Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=14,
        primary_key=True,
    )

    Hectare = models.CharField(
        help_text=_('Hectare'),
        max_length = 3,
        null=True,
    )

    AM = 'AM'
    PM = 'PM'

    Shift = models.CharField(
        help_text=_('Shift'),
        choices = (
            (AM, 'AM'),
            (PM, 'PM'),
        ),
        default = AM,
        max_length =2,
        null=True,
    )

    Date = models.DateField(
        help_text=_('Date'),
        null=True,
    )

    Hectare_Squirrel_Number = models.CharField(
        help_text=_('Hectare Squirrel Number'),
        max_length=10,
        null=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    BLANK = ''

    Age = models.CharField(
        help_text=_('Age'),
        choices = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (UNKNOWN, '?'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length=10,
        null=True,
        blank=True,
    )

    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMMON = 'Cinnammon'
    BLANK = ''

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary Fur Color'),
        choices = (
            (GRAY, 'Gray'),
            (BLACK, 'Black'),
            (CINNAMMON, 'Cinnammon'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length = 10,
        null=True,
        blank=True,
    )

    Gray = 'Gray'
    Black = 'Black'
    Cinnammon = 'Cinnammon'
    White = 'White'
    BlackCinnammon = 'Black, Cinnammon'
    BlackWhite = 'Black, White'
    BlackCinnammonWhite = 'Black, Cinnammon, White'
    CinnammonWhite = 'Cinnammon, White'
    GrayBlack = 'Gray, Black'
    BlackWhite = 'Black, White'
    GrayWhite = 'Gray, White'
    BLANK = ''

    Highlight_Fur_Color = models.CharField(
        help_text=_('Highlight Fur Color'),
        choices = (
            (Gray, 'Gray'),
            (Black, 'Black'),
            (Cinnammon, 'Cinnammon'),
            (White, 'White'),
            (BlackCinnammon, 'Black, Cinnammon'),
            (BlackWhite, 'Black, White'),
            (BlackCinnammonWhite, 'Black, Cinnammon, White'),
            (CinnammonWhite, 'Cinammon, White'),
            (GrayBlack, 'Gray, Black'),
            (BlackWhite, 'Black, White'),
            (GrayWhite, 'Gray, White'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length = 30,
        null=True,
        blank=True,
    )

    Combination_Fur = models.CharField(
        help_text=_('Combination of Primary and Highlight Color'),
        max_length = 100,
        null=True,
        default='+'
    )

    Color_Notes = models.CharField(
        help_text=_('Color Notes'),
        max_length=100,
        null=True,
        blank=True,
    )

    AboveGround = 'Above Ground'
    GroundPlane = 'Ground Plane'
    BLANK = ''

    Location = models.CharField(
        help_text=_('Location'),
        choices = (
            (AboveGround, 'Above Ground'),
            (GroundPlane, 'Ground Plane'),
            (BLANK, ''),
        ),
        default = BLANK,
        max_length=20,
        null=True,
        blank=True,
    )

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    Above_Ground_Sighter_Measurement = models.CharField(
        help_text=_('Above Ground Sighter Measurement'),
        max_length = 10,
        null=True,
        blank=True,
    )

    Specific_Location = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
        null=True,
        blank=True,
    )

    Running = models.CharField(help_text=_('Running'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Chasing = models.CharField(help_text=_('Chasing'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Climbing = models.CharField(help_text=_('Climbing'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Eating = models.CharField(help_text=_('Eating'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Foraging = models.CharField(help_text=_('Foraging'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)

    Other_Activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
        null=True,
        blank=True,
    )

    Kuks = models.CharField(help_text=_('Kuks'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Quaas = models.CharField(help_text=_('Quaas'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Moans = models.CharField(help_text=_('Moans'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Tail_Flags = models.CharField(help_text=_('Tail flags'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Tail_Twitches = models.CharField(help_text=_('Tail twitches'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Approaches = models.CharField(help_text=_('Approaches'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Indifferent = models.CharField(help_text=_('Indifferent'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Runs_From = models.CharField(help_text=_('Runs from'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    
    Other_Interactions = models.CharField(
        help_text=_('Other Interactions'),
        max_length=100,
        null=True,
        blank=True,
    )

    Lat_Long = models.CharField(
        help_text=_('Lat/Long'),
        max_length=50,
        null=True,
    )

    Zip_Codes = models.CharField(
        help_text=_('Zip Codes'),
        max_length=5,
        null=True,
        blank=True,
    )
    
    Community_Districts = models.CharField(
        help_text=_('Community Districts'),
        max_length=5,
        null=True,
        default='19',
    )

    Borough_Boundaries = models.CharField(
        help_text=_('Borough Boundaries'),
        max_length=5,
        null=True,
        default='4',
    )

    City_Council_Districts = models.CharField(
        help_text=_('City Council Districts'),
        max_length=5,
        null=True,
        default='19',
    )

    Police_Precincts = models.CharField(
        help_text=_('Police Precincts'),
        max_length=5,
        null=True,
        default='13',
    )

    def __str__(self):
        return self.name