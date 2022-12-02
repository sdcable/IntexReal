from django.shortcuts import render 
from django.shortcuts import HttpResponse
from .forms import serumEntryVizForm
import requests
import json

from Kidney.models import client
from Kidney.models import serum_entry
from Kidney.models import single_serving_food_item
from Kidney.models import dailydiary
from Kidney.models import journalentry
from django.shortcuts import redirect
from decimal import Decimal
#condition, single_serving_food_item, dailydiary, journalentry
#models 

#create views here
def index(request) :
    return render(request, 'index.html') #This will be our opening home page

def suggestions(request):
    return render(request, 'suggestions.html')

def serumViz(request, username):
    data = serum_entry.objects.filter(username=username)
    if request.method == 'POST':
        form = serumEntryVizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serumViz', username=username)
    else:
        form = serumEntryVizForm(request.POST)
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'serumViz.html', context)

def nutViz(request, diary_id, username):
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()
    thisDiary = dailydiary.objects.get(dd_id=diary_id)
    myClient = client.objects.get(username=username)
    #eatFood = single_serving_food_item.objects.filter(food_name=entry.food_name)
    #myClient = client.objects.get(username=thisDiary.username)

    #dailydiarys = dailydiary.objects.get(dd_id=diary_id) #dailydiaries: 11-30-2022 Jonny Cache --> dailydiaries.username = Jonny Cache
    #y = dailydiarys.username #Jonny Cache
    #clients = client.objects.all()
    #clients = client.objects.get(username=dailydiarys.username) #(username=y)
    
    #water loop
    waterNutrient = 0.0
    foods = {}
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                waterNutrient = waterNutrient + (float(food[iCount].water) * float(entry[iCount2].consumed_serving_size))                
            iCount += 1
        iCount2 += 1
    
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()
    #Protein loop
    proteinNutrient = 0.0
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                proteinNutrient = proteinNutrient + (float(food[iCount].protein) *  float(entry[iCount2].consumed_serving_size))
            iCount += 1
        iCount2 += 1
    
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()
    
    #Sodium loop
    sodiumNutrient = 0.0
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                sodiumNutrient = sodiumNutrient + (float(food[iCount].sodium) *  float(entry[iCount2].consumed_serving_size))
            iCount += 1
        iCount2 += 1
    
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()
    
    #Potassium loop
    waterNutrient = 0.0
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                waterNutrient = waterNutrient + (float(food[iCount].water)  *  float(entry[iCount2].consumed_serving_size))
            iCount += 1
        iCount2 += 1
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()

    #Phosphorus loop
    phosphorusNutrient = 0.0
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                phosphorusNutrient = phosphorusNutrient + (float(food[iCount].phosphorus) *  float(entry[iCount2].consumed_serving_size))
            iCount += 1
        iCount2 += 1
    
    entry = journalentry.objects.filter(dd_id=diary_id)
    food = single_serving_food_item.objects.all()
    
    #potassium loop
    potassiumNutrient = 0.0
    
    iCount2 = 0
    while iCount2 < len(entry):
        iCount = 0
        while iCount < len(food):
            if entry[iCount2].food_name == food[iCount]:
                potassiumNutrient = potassiumNutrient + (float(food[iCount].potassium) *  float(entry[iCount2].consumed_serving_size))
            iCount += 1
        iCount2 += 1

    if myClient.gender == 'male':
        wLimit = 3700 - waterNutrient
    else:
        wLimit = 2700 - waterNutrient
    proLimit = .6*float(myClient.weight)*0.4536 - proteinNutrient
    sLimit = 2.3 - sodiumNutrient
    phosLimit = 1.0 - phosphorusNutrient
    potLimit = 3.0 - potassiumNutrient

    context = {
        'journal': entry,
        'food': food,
        'waterNutrient': waterNutrient,
        'proteinNutrient': proteinNutrient,
        'sodiumNutrient' : sodiumNutrient,
        'phosphorusNutrient': phosphorusNutrient,
        'potassiumNutrient': potassiumNutrient,
        'myClient': myClient,
        'wLimit': wLimit,
        'proLimit': proLimit,
        'sLimit': sLimit,
        'phosLimit': phosLimit,
        'potLimit': potLimit,
        'thisDiary': thisDiary
        #'client': clients
    }
    #return  HttpResponse(coolVar)     #HttpResponse(entry[0].food_name)
    return render(request, 'nutViz.html', context)

def personal(request):
    data = client.objects.all()

    context={
        "client": data
    }
    return render(request, 'personal.html', context)

def clientindex(request):
    return render(request, 'clientindex.html')

def viewFood(request):
    food = single_serving_food_item.objects.all()
    
    context= {
        'food': food
    }
    return render(request, 'viewFood.html', context)



def addEntryDestination(request):
    if request.method == "POST":
        new_client = client()

        new_client.username = request.POST['username']
        new_client.first_name = request.POST['first_name']
        new_client.last_name = request.POST['last_name']
        new_client.email = request.POST['email']
        new_client.dateOfBirth = request.POST['dateOfBirth']
        new_client.gender = request.POST['gender']
        new_client.race = request.POST['race']
        new_client.weight = request.POST['weight']
        
        new_client.save()

        data = client.objects.all()

        context={
            "client": data
        }
        return render(request, 'personal.html', context)
    else:
        return render(request, 'clientindex.html') 

def addDiaryPageView(request):
    entry = dailydiary.objects.all()

    context={
        "uName" : entry
    }
    return render(request, 'addDiary.html', context)

def addEntryPageView(request, diary_id):
    entry = journalentry.objects.all()
    diary = dailydiary.objects.get(dd_id=diary_id)
    context={
        "data" : entry,
        "myDiary" : diary
    }
    return render(request, 'addEntry.html', context)

def addFoods(request):
    if request.method == "POST":
        new_food = single_serving_food_item()

        new_food.food_name = request.POST['food_name']
        new_food.sodium = request.POST['sodium']
        new_food.potassium = request.POST['potassium']
        new_food.protein = request.POST['protein']
        new_food.water = request.POST['water']
        new_food.phosphorus = request.POST['phosphorus']
        new_food.serving_unit = request.POST['serving_unit']
        new_food.serving_size_amount = request.POST['serving_size_amount']
        
        new_food.save()

        food = single_serving_food_item.objects.all()
    
        context= {
            'food': food
        }
        return render(request, 'viewFood.html', context)
    else:
        return render(request, 'addFoods.html')

def addClientPageView(request):
    if request.method == "POST":
        new_client = client()

        new_client.username = request.POST['username']
        new_client.first_name = request.POST['first_name']
        new_client.last_name = request.POST['last_name']
        new_client.email = request.POST['email']
        new_client.dateOfBirth = request.POST['dateOfBirth']
        new_client.gender = request.POST['gender']
        new_client.race = request.POST['race']
        new_client.weight = request.POST['weight']
        
        new_client.save()

        data = client.objects.all()

        context={
            "client": data
        }
        return render(request, 'personal.html', context)
    else:
        return render(request, 'addClient.html')

def updateClientPageView(request, clientusername):
    if request.method == 'POST' :
        usernamehere = request.POST['username']

        clients = client.objects.get(username=usernamehere)

        clients.first_name = request.POST['first_name']
        clients.last_name = request.POST['last_name']
        clients.username = request.POST['username']
        clients.email = request.POST['email']
        clients.gender = request.POST['gender']
        clients.race = request.POST['race']
        clients.weight = request.POST['weight']
        clients.condition_name = request.POST['condition_name']

        clients.save()

        data = client.objects.all()

        context={
            "client": data
        }
        return render(request, 'personal.html', context)
    else:
        data = client.objects.get(username=clientusername)

        context={
            "client": data
        }
        return render(request, 'updateClient.html', context)

def addFoodTest(request):

    foodname = request.POST['food_name']
    url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=sCuiTtIVzfYkYZQ2O8Iv2xnlGWeELnB9Z65oQdMI&query=%s" %(foodname)
    response = requests.request("GET", url) # , headers=headers, data=payload
    json_data = json.loads(response.text) #loads the response text (all the json we printed out in the code block above into a variable called json_data)
    iCount = 0
    #2116771
    while json_data['foods'][iCount]['dataType'] != 'Branded':
        iCount += 1
    serving_unit = json_data['foods'][iCount]['servingSizeUnit']
    serving_size_amount = json_data['foods'][iCount]['servingSize']
    if serving_unit == 'g':
        serving_unit = 'grams'
    #add all other serving units    DON'T FORGET
    iCount2 = 0
    while json_data['foods'][iCount2]['dataType'] != 'Survey (FNDDS)':
            iCount2 += 1
    value = json_data['foods'][iCount2]['fdcId']
    url2 = 'https://api.nal.usda.gov/fdc/v1/food/' + str(value) + '?nutrients=203,255,305,306,307&api_key=sCuiTtIVzfYkYZQ2O8Iv2xnlGWeELnB9Z65oQdMI'
    response2 = requests.request("GET", url2)
    json_data2 = json.loads(response2.text)
    newDict = dict()
    testing = json_data2['foodNutrients']
    mineralList = ['Sodium, Na','Potassium, K', 'Phosphorus, P'] # 134.00 --> 0.13400
    iCount = 0
    while iCount < len(json_data2['foodNutrients']):
        value2 = json_data2['foodNutrients'][iCount]['nutrient']['name']
        value3 = json_data2['foodNutrients'][iCount]['amount']
        if value2 in mineralList:
            value3 = value3 / 1000
        value3 = serving_size_amount/100 * value3 #Standardizing values according to serving size
        newDict[value2] = round(value3, 4)
        iCount += 1
    food = single_serving_food_item()
    food.food_name = request.POST['food_name']
    food.sodium = newDict['Sodium, Na']
    food.potassium = newDict['Potassium, K']
    food.protein = newDict['Protein']
    food.water = newDict['Water']
    food.phosphorus = newDict['Phosphorus, P']
    food.serving_unit = serving_unit
    food.serving_size_amount = round(serving_size_amount,2)
    food.save()

    singleserve = single_serving_food_item.objects.get(food_name=request.POST['food_name'])
    daily = dailydiary.objects.get(dd_id=request.POST['dd_id'])

    newjournal = journalentry()

    newjournal.meal_type = request.POST['meal_type']
    newjournal.food_name = singleserve
    newjournal.consumed_serving_size = request.POST['consumed_serving_size']
    newjournal.dd_id = daily

    newjournal.save()

    return redirect('personal')



def addDailyDiary(request):
    if request.method == "POST":
        diary = dailydiary()

        clientUsername = client.objects.get(username=request.POST['username'])

        diary.username = clientUsername
        diary.date = request.POST['date']

        diary.save()

        return redirect('personal')

def showDiariesPageView(request, username):
    data = dailydiary.objects.filter(username=username)
    clients = client.objects.filter(username=username)

    context={
        "diary": data,
        "client": clients
    }
    return render(request, 'showDiary.html', context)

def showEntryPageView(request, diary_id):
    entry = journalentry.objects.filter(dd_id=diary_id)
    thisDiary = dailydiary.objects.get(dd_id=diary_id)

    context = {
        "record" : entry,
        "myDiary" : thisDiary
    }
    return render(request, 'showEntry.html', context)

def editEntryPageView(request, journal_id):
    data = journalentry.objects.get(journal_entry_id=journal_id)

    context = {
        "record" : data
    }
    return render(request, 'editEntry.html', context)

def deleteEntry(request, journal_id):
    data = journalentry.objects.get(journal_entry_id=journal_id)
    dd = dailydiary.objects.get(dd_id=str(data.dd_id))
    #data_id = 21


    data.delete()
    
    return redirect('showDiaries', username=dd.username)
    #return HttpResponse(dd.username)

def updateEntryPageView(request):
    if request.method == 'POST':
        journal_id = request.POST['journal_id']
        thisEntry = journalentry.objects.get(journal_entry_id=journal_id)
        dd_id = request.POST['dd_id']
        thisEntry.meal_type = request.POST['meal_type']
        thisEntry.consumed_serving_size = request.POST['consumed_serving_size']
        thisEntry.save()

        data = journalentry.objects.get(journal_entry_id=journal_id)
        dd = dailydiary.objects.get(dd_id=str(data.dd_id))

        return redirect('showDiaries', username=dd.username)
