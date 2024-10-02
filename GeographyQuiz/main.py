print('Hello there, what is your name?')
type_in_name=input()
print(f'Hello there,{type_in_name},lets see how many geography questions you can get correct!')
score=0


question1=input("Name a country that starts with the letter E, its capital city is called Asmara, and it is located in the Horn of Africa:").upper()
if question1=="ERITREA":
    score += 1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question2=input("Name a country that starts with the letter R, its capital city is Moscow,and it is located in Eastern Europe:").upper()
if question2==("RUSSIA"):
    score +=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question3=input("Name a country that starts with the letter J, its capital city is Tokyo,and it is located in Eastern Asia:").upper()
if question3==("JAPAN"):
    score +=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question4=input("Name a country that starts with the letter M, its capital city is Mexico City,and it is located in North America:").upper()
if question4==("MEXICO"):
    score +=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question5=input("Name a country that starts with the letter I, its capital city is New Delhi,and it is located in South Asia:").upper()
if question5==("INDIA"):
    score +=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question6=input("Name a country that starts with the letter N, its capital city is Abuja,and it is located in West Africa:").upper()
if question6==("NIGERIA"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question7=input("Name a country that starts with the letter C, its capital city is Beijing,and it is located in East Asia:").upper()
if question7==("CHINA"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question8=input("Name a country that starts with the letter G, its capital city is Berlin,and it is located in Central Europe:").upper()
if question8==("GERMANY"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question9=input("Name a country that starts with the letter C, its capital city is Havana,and it is located in the Caribbean:").upper()
if question9==("CUBA"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question10=input("Name a country that starts with the letter B, its capital city is Brasília,and it is located in South America:").upper()
if question10==("BRAZIL"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question11=input("Name a country that starts with the letter E, its capital city is London,and it is located in Western Europe:").upper()
if question11==("ENGLAND"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question12=input("Name a country that starts with the letter F, its capital city is Paris,and it is located in Western Europe:").upper()
if question12==("FRANCE"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question13=input("Name a country that starts with the letter S, its capital city is Riyadh,and it is located in the Middle East:").upper()
if question13==("SAUDI ARABIA"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question14=input("Name a country that starts with the letter P, its capital city is Ramallah,and it is located in the Middle East:").upper()
if question14==("PALESTINE"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

question15=input("Name a country that starts with the letter I, its capital city is Jerusalem,and it is located in the Middle East:").upper()
if question15==("ISRAEL"):
    score+=1
    print(f'Correct, your score is now {score}!')
else:
    print(f'Incorrect, your score is now {score}!')

Total=(score/15)*100
print(f'\nCongrats, you got a total of {Total}% correct!')

