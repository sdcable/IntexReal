from django.db import models

# Create your models here.
#how to implement choices
#https://stackoverflow.com/questions/31130706/dropdown-in-django-model
gender_choices = (
    ('female', 'FEMALE'),
    ('male', 'MALE'),
    ('other', 'OTHER'),
    ('none', 'NONE'),
)

race_choices = (
    ('white', 'WHITE'),
    ('hispanic', 'HISPANIC'),
    ('black', 'BLACK'),
    ('asian', 'ASIAN'),
    ('multiple races', 'MULTIPLE RACES'),
    ('american indian/alaskan native','AMERICAN INDIAN/ALASKAN NATIVE'),
    ('native hawaiian/pacific islander','NATIVE HAWAIIAN/PACIFIC ISLANDER'),
    ('none', 'NONE'),
)

condition_choices = (
    ('diabetes','DIABETES'),
    ('hypertension','HYPTERTENSION'),
    ('cardiovasular disease','CARDIOVASCULAR DISEASE'),
    ('hyperlipidemia','HYPERLIPIDEMIA'),
    ('none', 'NONE')
)

class client(models.Model):
    username = models.CharField(max_length=25, null=False, primary_key=True, default=None)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    dateOfBirth = models.DateField(auto_now_add=False)
    gender = models.CharField(max_length=6, choices=gender_choices, default=None)
    race = models.CharField(max_length=33, choices=race_choices, default=None)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    condition_name = models.CharField(max_length=32, choices=condition_choices, blank=True, null=True, default='none')


    def __str__(self):
        #return (self.first_name + " " + self.last_name)
        return (self.username)
    
    class Meta: #This is the real table name in the database
        db_table = 'client'

        
serving_unit_choices = (
    ('cup','CUP'),
    ('tablespoon','TABLESPOON'),
    ('teaspoon','TEASPOON'),
    ('grams','GRAMS'),
    ('slice','SLICE'),
    ('ounce','OUNCE'),
    ('fluid ounces','FLUID OUNCES'),
    ('liters','LITERS'),
    ('milliliters','MILLILITERS'),
    ('whole','WHOLE'),

)

class serum_entry(models.Model):
    serum_id = models.AutoField(primary_key=True, default=None)
    username = models.ForeignKey('client', null=False, blank=False, on_delete=models.CASCADE)
    serum_date = models.DateField(auto_now_add=False)
    serum_potassium = models.DecimalField(max_digits=20, decimal_places=4)
    serum_phosphorus = models.DecimalField(max_digits=20, decimal_places=4)
    serum_sodium = models.DecimalField(max_digits=20, decimal_places=4)
    serum_creat = models.DecimalField(max_digits=20, decimal_places=4)
    serum_alb = models.DecimalField(max_digits=20, decimal_places=4)
    serum_blood_sugar = models.DecimalField(max_digits=50, decimal_places=4)
    
    class Meta: #This is the real table name in the database
        db_table = 'serum_entry'

class single_serving_food_item(models.Model):
    food_name = models.CharField(max_length=50, primary_key=True, auto_created=False)
    sodium = models.DecimalField(max_digits=20, decimal_places=4)
    potassium = models.DecimalField(max_digits=20, decimal_places=4)
    protein = models.DecimalField(max_digits=20, decimal_places=4)
    water = models.DecimalField(max_digits=20, decimal_places=4)
    phosphorus = models.DecimalField(max_digits=20, decimal_places=4)
    serving_unit = models.CharField(max_length=50, choices=serving_unit_choices)
    serving_size_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return (self.food_name)
    
    class Meta: #This is the real table name in the database
        db_table = 'single_serving_food_item'


class dailydiary(models.Model):
    dd_id = models.AutoField(primary_key=True, default=None)
    username = models.ForeignKey('client', null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)

    class Meta:
        db_table = 'dailydiary'
    
    #@property
    #def date_and_username(self):
    #    return '%s %s' %(self.date, self.username)

    def __str__(self):
        return (str(self.dd_id))


meal_type_choices = (
    ('breakfast','BREAKFAST'),
    ('lunch','LUNCH'),
    ('dinner','DINNER'),
    ('snack','SNACK'),
)

class journalentry(models.Model):
    journal_entry_id = models.AutoField(primary_key=True, default=None)
    meal_type = models.CharField(choices=meal_type_choices, max_length=40)
    food_name = models.ForeignKey('single_serving_food_item', null=False, blank=False, on_delete=models.CASCADE)
    consumed_serving_size = models.DecimalField(max_digits=4, decimal_places=2)
    dd_id = models.ForeignKey('dailydiary', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.food_name) + " " + str(self.meal_type) + " " + str(self.dd_id))
    
    class Meta: #This is the real table name in the database
        db_table = 'journal_entries'



#class journalEntry(models.Model):

#to store passwords
#https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django