import models


class Category (object):

    def __init__(self):
        
        self.products = ["Apparel and Jewelery", "Baby and Toys", "Beauty and Health", "Books, Movies and Media", "Consumer Electronics", "Food", "Home and Garden", "Motor Vehicles", "Novelty", "Office Products and Supplies", "Software and Apps", "Sports and Outdoors", "Other Product"]

        self.services = ["Bars and Nightlife", "Beauty and Hair", "Child and Daycare", "Cleaning and Maid", "Educational", "Financial and Insurance", "Fitness", "Healthcare", "IT and Technical", "Legal", "Live Entertainment", "Planning and Creative", "Real Estate", "Repair and Maintenance", "Restaurants and Fast Food", "Retail and Sellers", "Sports, Recreation and Outdoors", "Travel and Vacation", "Web and Internet", "Other Service"]

        self.events = ["Arts", "Charity", "Entertainment", "Food and Drink", "Holiday and Celebration", "Social and Professional", "Sports and Outdoors", "Other Event"]


        
        # To get the keys below, take name above, remove spaces and nonalpha characters and lowercase all letters
        # This convention is used throughout the view code


        self.hashmapper = {"apparelandjewelery": models.PApparel, "babyandtoys": models.PBaby, "beautyandhealth": models.PBeauty, "booksmoviesandmedia": models.PMedia, "consumerelectronics": models.PElectronics, "food": models.PFood, "homeandgarden": models.PHome, "motorvehicles": models.PVehicles, "novelty": models.PNovelty,  "officeproductsandsupplies": models.POffice, "softwareandapps": models.PSoftware, "sportsandoutdoors": models.PSports, "otherproduct": models.POther,"barsandnightlife": models.SBars, "beautyandhair": models.SBeauty, "childanddaycare": models.SChild, "cleaningandmaid": models.SCleaning, "educational": models.SEducational, "financialandinsurance": models.SFinancial, "fitness": models.SFitness, "healthcare": models.SHealthcare, "itandtechnical": models.SIT, "legal": models.SLegal, "liveentertainment": models.SLive, "planningandcreative": models.SCreative, "realestate": models.SReal, "repairandmaintenance": models.SRepair, "restaurantsandfastfood": models.SRestaurants, "sportsrecreationandoutdoors": models.SSports, "retailandsellers": models.SStores, "travelandvacation": models.STravel, "webandinternet": models.SWeb, "otherservice": models.SOther, "arts": models.EArts, "charity": models.ECharity, "entertainment": models.EEntertainment, "foodanddrink": models.EFood, "holidayandcelebration": models.EHoliday, "socialandprofessional": models.ESocial, "sportsandoutdoors": models.ESports , "otherevent": models.EOther}
        
        
        
    def nametomodel(self, name):
    
        import re
        
        return self.hashmapper[ re.sub(r'[^a-zA-Z]', '', name).lower() ]
    
    
    # less efficient, but is called infrequently
    def modeltoname(self, model):
        
        for key in self.hashmapper.keys():

            if self.hashmapper[key] == model:
                return key
    
        
    
    

ReviewCategories = Category()



