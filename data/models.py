from django.db import models

class Category(models.Model):
    px_id = models.IntegerField()
    name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    px_slug = models.CharField(max_length=255)


class Tag(models.Model):
    px_id = models.IntegerField()
    name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    category = models.ForeignKey(
        'Category',
        db_column = 'category_id',
        on_delete=models.PROTECT
    )
    px_slug = models.CharField(max_length=255)


class Offer(models.Model):
    PX_SELL = 'sell'
    PX_BUY = 'buy'
    OFFER_TYPE = [
        (PX_SELL, 'Sell'),
        (PX_BUY, 'Buy')
    ]
    BTC = 'BTC'
    USDT = 'USDT'
    CURRENCIES = [
        (BTC, 'Bitcoin'),
        (USDT, 'Tether')
    ]

    px_id = models.CharField(max_length=255)
    verified = models.BooleanField()
    sell_cur = models.CharField(
        'cryptoCurrencyCode', max_length=128, choices=CURRENCIES
    )
    buy_cur = models.CharField('fiatCurrencyCode', max_length=128)
    margin = models.FloatField()
    price_per_cur = models.FloatField('pricePerUsd'),
    require_verified_id: models.BooleanField()
    payment_method_name = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', related_name='offers', blank=True)
    category = models.ForeignKey(
        'Category',
        db_column = 'category_id',
        on_delete=models.PROTECT
    )
    payment_method_label = models.CharField(max_length=255)
    username =  models.CharField(max_length=255)
    score = models.FloatField()
    last_seen = models.CharField('lastSeenString', max_length=255)
    average_trade_speed = models.CharField("releaseTimeMedianHumanize", max_length=255)
    user_timezone = models.CharField(max_length=255)
    offer_type = models.CharField(
        max_length=128, choices=OFFER_TYPE, default=PX_SELL
    )
    offer_detail = models.ForeignKey(
        'OfferDetail',
        db_column = 'offer_detail_id',
        on_delete=models.CASCADE
    )


class OfferDetail(models.Model):
    feedback_negative = models.IntegerField()
    feedback_positive = models.IntegerField()
    predefined_amount = models.JSONField(blank=True)
    fiat_amount_range_min = models.IntegerField()
    fiat_amount_range_max = models.IntegerField()
    fiat_price_per_btc = models.FloatField()
    price_per_btc = models.FloatField()
    fee_percentage = models.IntegerField()
    payment_method_group_id = models.IntegerField()
    percent_per_usd = models.FloatField()
    require_full_name_visibility = models.BooleanField()
    default_flow_type = models.CharField(max_length=255)