#VARIABLES

total_area=687500

potato_eff=3.245
carrot_eff=5.344
onion_eff=2.98
pepper_eff=9.29
tomatoes_eff=13.91

#Half year cycle used, R is the rotation you can do per half year
onion_r=2
potato_r=2
pepper_r=1
tomato_r=2
carrot_r=2

#Calculate constants for different crops
A1 = potato_eff * potato_r  
A2 = carrot_eff * carrot_r
A3 = onion_eff * onion_r
A4 = pepper_eff * pepper_r
A5 = tomatoes_eff * tomato_r

#Water Usage per Week per m^2
W_Onion = 0.254
W_Potato = 0.32
W_Pepper = 0.254
W_Tomato = 0.32
W_Carrot = 0.25 

#Growing Time
G_Onion = 95
G_Potato = 110
G_Pepper = 125
G_Tomato = 90
G_Carrot = 75 



#Winter & summer calculate area to give per crop
def Calculate_area_per_crop(constant_List):

  #Calculate the Ratio
  #crops = ["Potatoes", "Onions", "Peppers", "Tomatoes"]
  x1 = 1
  x2 = (x1 * constant_List[0]/constant_List[1]) * 0.5
  x3 = (x1 * constant_List[0]/constant_List[2]) * 0.5 * 0.5
  x4 = (x1 * constant_List[0]/constant_List[3]) * 0.5

  #Calculte areas for different crops using the ratio
  area_for_x1 = total_area/(x1+x2+x3+x4)
  area_for_x2 = area_for_x1 * x2
  area_for_x3 = area_for_x1 * x3
  area_for_x4 = area_for_x1 * x4
      
  area_division_list = [area_for_x1,area_for_x2,area_for_x3,area_for_x4]

  #print(sum(area_division_list)) #testing (Adds up to total area)
  
  return area_division_list


def water_Usage(area_per_crop,season):
  #VPR = volume per rotation

  if (season == 'W'):
    VPR_first = 0.32 * area_per_crop[0] * G_Potato/7
  elif (season == 'S'):
    VPR_first = 0.25 * area_per_crop[0] * G_Carrot/7
    
  VPR_Onion = 0.254 * area_per_crop[1] * G_Onion/7 #Water use per day per crop per m^2
  VPR_Pepper = 0.254 * area_per_crop[2] * G_Pepper/7
  VPR_Tomato = 0.32 * area_per_crop[3] + G_Tomato/7

  #Water Usage per crop 
  total_Water_Usage = [VPR_first, VPR_Onion, VPR_Pepper, VPR_Tomato] 
  
  return total_Water_Usage




def main():
  season = input("What is the current Season: W(for Winter) or S(for Summer): ")
  season_str = ""
  if (season == 'W'):
    season_str = "Winter"
    crops = ["Potatoes", "Onions", "Peppers", "Tomatoes"]
    constant_List = [A1,A3,A4,A5]
  elif (season == 'S'):
    season_str = "Summer"
    crops = ["Carrots", "Onions", "Peppers", "Tomatoes"]
    constant_List = [A2,A3,A4,A5]
  else:
    print("Please Select W(for Winter) or S(for Summer)")

  area_per_crop = Calculate_area_per_crop(constant_List)


  for i in range(len(crops)):
    print("Area to be used for {0:>8}: {1:.2f}".format(crops[i],area_per_crop[i]))

  total_Water_Usage_list = water_Usage(area_per_crop,season)
  
  print("Water used in {0} in m^3:  {1:.2f}".format(season_str , sum(total_Water_Usage_list)))

  if (season == 'W'):
    print("Weight of Potatoes produced in KG: ",(area_per_crop[0]*A1))
  elif (season == 'S'):
    print("Weight of Carrots produced in KG: ",(area_per_crop[0]*A2))

  print("Number of CANS produced in a year: ", int(area_per_crop[0]*A1*100/2))

if __name__ == "__main__":
    main()