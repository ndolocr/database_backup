from django.db import models

# Create your models here.
class Rule(models.Model):
    class Meta:
        db_table = "rules"

    action = models.TextField()
    conditions = models.TextField()
    priority = models.IntegerField()
    description = models.TextField()
    rule_id = models.CharField(max_length = 512)
    ruleNamespace = models.CharField(max_length = 256)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Request(models.Model):
    class Meta:
        db_table = 'requests'
        
    decision = models.TextField(null=True)    
    request_payload = models.TextField(null=True)
    response_message = models.TextField(null=True)
    response_payload = models.TextField(null=True)
    cr_account = models.CharField(max_length=255,  null=True)
    dr_account = models.CharField(max_length=255,  null=True)
    name_space = models.CharField(max_length=255,  null=True)
    transaction_time = models.DateTimeField(auto_now_add=False)
    response_status = models.CharField(max_length=255,  null=True)
    score = models.DecimalField(max_digits=15, decimal_places=2)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)