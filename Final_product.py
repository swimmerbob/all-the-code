import time
import re
import sys
import readline
bad_counter = 0
good_counter = 0
achievements = 0
index = 0
user_input = str()
repeat_sad = False
death = False
angry = False
suicide = False
murder = False
bullied = False
pattern = re.compile('\W')
new_word = str()
good_keywords = ["good","great","excellent","positive","hopeful","hopefull","awesome","happy","joyful","joyfull","excited","pleased","at peace","calm","delightful","cheerful","content","super", "ok"] 
bad_keywords = ["bad","angery","angry","negative", "sad", "depresed", "suicidal", "horrible", "emo","kill me", "angry","dejected", "depressed", "deprived", "desolate", "despair", "desperate", "despicable", "detestable", "diminished", "disappointed", "discouraged", "disgusting", "disillusioned", "disinterested", "dismayed", "dissatisfied", "distressed", "distrustful", "dominated", "doubtful", "dull","shitty","unloved","unworthy","useless","worthless","alone","angry","cold"]
agreeing_keywords = ["maybe","ok","meh","yes","yeah","i guess","ok","fine","alright","ight","yup","sure","yeah","yuh","yep","affirmative","ya", "yea","yeet","hai","k",'ya',"indubitably"]
disagreeing_keywords = ["no","nope","naw","hell naw","nay","nix","never","nein","non","no reason","not","never"]
pronoun_list = ["he","his","him","her", "she","they","their","mom","dad","uncle","aunt","grandma",'granpa','grandpa','brother','sister','friend','cousin','best friend','pet','dog','cat','bird','turtle','ma','paw','pa',"has","hes","shes",'moms','dads','brothers',"them","all","everyone","him","every","her","someone","anybody"]
self_keywords = ["i","me","myself","am","are"]
angry_keywords=["mad",'angry','angery','aggressive',"psychothic",'unstable','pissed off']
def useablestring():
    global user_input
    user_input =  re.sub(pattern, '', user_input)
    user_input = user_input.lower()
i = 0
while i < 6:
    print "loading","."*i
    time.sleep(.4)
    sys.stdout.write("\033[F")
    i +=1
feeling = str()
while user_input != "quit":
    
    print "                                        Hi I'm Chat Bot, your robotic friend and helper. How can I help you today?"
    print"""" Here is my library for you to choose from:
                                                      "info" for tips oh how to talk to people with depresion/ handling depresion
                                                      "advice" for cool stuff to do with people with depresion and more
                                                      "links" for external help and hotlines
                                                      "chat" for you to talk to me
                                                      "music" to listen to some calming music
                                                      "stories" to see how other people deal with depression
                                                      "view achievements" to view all achievements
                                                      "quit" to end this sesion
                                                      """
    user_input = raw_input("Please choose something from my library!: ")
    if user_input == "info":
        sys.stdout.write("\033[F")
        print """Depression is an illness that can cause and affects someone's actions, mood, concentration, sleep and appetite.
        The symptoms are tense feeling like the perception of physical pain with the heart and stomach area. Major depression should 
        be teated as a real illness and failure to notice it could lead to increasing sadness and lack of interest to do anything. 
        Major Depression and attempts of suicide are found to be common among schizophrenic patients. 
        Depression found in men may also be found and not treated because from in a cultural standpoint they are the ones that are expected to have lack of emotion and to hold the emotions in.
        Ask your doctor or see a council if you have Clinical depression.
        """
        time.sleep(10)
    if user_input == "advice":
        sys.stdout.write("\033[F")
        print """This app not supposed to cure your depression, but it is supposed to help with it.
        If this app does not help, please seak help from a counselor or a medical professional.
        One of the best things you can do is talk about how you feel to someone and have them listen to you.
        Stop thinking about the worst-case scenario, and all the things that could possibly go 
        wrong. Instead, step back and take a realistic look at life. Nothing is ever the end of the 
        world, after all.
        A lot of bad moods are worsened by the fact that you keep thinking about them, and 
        feeling sorry for yourself. Stop being so concerned with how you feel. Youll never 
        change things by getting stuck in thinking about them  take action instead, to make 
        things better.
        Its very difficult to be depressed if you can write a long list of all the things you love in 
        your life. Not so much a mental trick as a realization of what youre very lucky to have 
        despite this tough time youre going through.
        When youre feeling low, its easy to get caught up in believing that bad things are 
        happening because of you. Dont allow yourself to believe that youre a victim. You 
        have the power to choose how you react to problems  and thats the most powerful 
        thing of all.
        When thinking of self harm or suicide, think about the hurt youre causing yourself but also think of
        the people close to you and how they would feel. Don't make other people get hurt just because you are. You 
        know how much it hurts so dont pass it on. Dont make them suffer.
        Try getting some sleep doctors recommend sleep to help with stress.
        Another thing that you could try is exercies. You may not want to do so, but 30 minutes each day will help, even if it's just for a little bit.
        """
        time.sleep(10)
        print "Congratulations for getting an achievement! : the advice getter"
        achievements = achievements +1 
        if achievements == 1:
            print """
             _________________  
            |     Tier 1      |
            |                 |
            | CONGRATULATIONS |
            |                 |
            |_________________|
"""
        if achievements == 2:
            print """

                    ___________ 
          ______   |   Tier 2  |   ______
         |      |__|           |__|      | 
         |       _CONGRATULATIONS_       |  
         |______|  |           |  |______|
                   |___________| 
"""
        if achievements == 3:
            print """


       Tier 3                 
                   ( )   
       _______    / / 
 ( )  |\      \  / /
  \ \_| \______\/_/
   \__) |       |
      | |       |
      \ |       |
       \|_______|
        | |   \ |
       ( (    | |
        \ \   | |
        ( )   | |
              ( ) 
CONGRATULATIONS THIS IS THE FINAL TIER!
"""
    if user_input == "links":
        sys.stdout.write("\033[F")
        print """This link is for general information about suicide and for some encouragment:
        http://suicidepreventionlifeline.org/
        This link is to talk to someone about how you are feeling:
        https://suicidepreventionlifeline.org/chat/ 
        This link is for general trick to fight depresion:
        https://www.lifehack.org/articles/lifestyle/15-mental-tricks-fight-depression.html 
        here is a link on how to help someone with depresion:
        https://www.verywellmind.com/what-to-say-when-someone-is-depressed-1067474
        This is a phone number you can call to also help you out:
        1-800-273-8255 
        """
        time.sleep(6)
    if user_input == "chat":
        sys.stdout.write("\033[F")
        user_input = raw_input( "In one word, how would you say you are feeling today?: ")
        feeling = user_input
        useablestring()
        if user_input in good_keywords:
            print "It's great that you are feeling", user_input + "!"
            user_input = raw_input("Do you know a friend who is sad or distressed?: ")
            useablestring()
            new_word = user_input
            if user_input in agreeing_keywords:
                print "So what is going on with them?: "
                user_input = raw_input()
                story_list = user_input.split(" ")
                user_story = [item.lower() for item in story_list]
                user_story = [re.sub(pattern, '', item) for item in user_story]
                if user_story[0] == "nothing":
                     print """"It is posible that they are experienceing a horomone inbalance. I recomend if you havent already, go visit a doctor and see what they tell you.
                     If you already have, I recommend checking out the advice or links tab for some more help."""
                else:
                    while index < len(user_story):
                        if user_story[index] in bad_keywords:
                            if user_story[index-1] == "always":
                                repeat_sad = True
                                bad_counter += 1
                        if user_story[index] in good_keywords:
                            if user_story[index-1] in disagreeing_keywords:
                                bad_counter += 1
                            else:
                                good_counter += 1
                        if user_story[index] == "died":
                            if user_story[index-1] in pronoun_list:
                                person = user_story[index-1]
                                death = True
                        if user_story[index] in angry_keywords:
                            if user_story[index-1] == "is":
                                angry = True
                            if user_story[index-1] == "always":
                                angry = True
                            if user_input[index-1] in self_keywords:
                                angry = True
                        if user_story[index] == "kill":
                            if user_story[index+1] in self_keywords:
                                suicide = True
                            if user_story[index+1] in pronoun_list:
                                murder = True
                        if user_story[index] == "bullied":
                            bullied = True
                        index += 1
                    if bullied == True:
                        print"From what i understand your friend is getting bullied. is that true?"
                        user_input=raw_input()
                        if user_input in agreeing_keywords:
                            print"""When getting bullied it is important to understand the seriousness of the situation. 
                            it is entirely posible a joke went to far and a sime request to stop may be enough.
                            in serious cases it is nessesary to get someone of higher authority to intervene.
                            Dont let this situation to affect your mood. only you are in control of your emotions."""
                    if murder == True:
                        print"From what I understand your friend wants to kill someone, is this true?"
                        user_input=raw_input()
                        if user_input in agreeing_keywords:
                            print"If they are serious about this i reccomend calling the police even if they are your best friend. murder is never ok or justifiable."
                        if user_input in disagreeing_keywords:
                            print"I am sorry for thinking this."
                    if suicide == True:
                        print"""
                        Suicide is never the answer.life never has no meaning anymore and there is always a point or a reason to live.
                        Friends and family are always there to talk to you. Dont feel like even if you have made past mistakes that they wolnt help you.
                        there is always hope somewhere, there is always someone to talk to. if you feel up to it there are several links and phone numbers under the links catagory.
                        """
                    if repeat_sad == True:
                        print""" 
                            I recomend telling your friend that
                         A lot of bad moods are worsened by the fact that you keep thinking about them, and 
        feeling sorry for yourself. Stop being so concerned with how you feel. You'll never 
        change things by getting stuck in thinking about them  take action instead, to make 
        things better.
        """
                    
                    if bad_counter > good_counter:
                        print """
                        I recomend telling your friend that Its very difficult to be depressed if you can write a long list of all the things you love in 
        your life. Not so much a mental trick as a realization of what youre very lucky to have 
        despite this tough time youre going through.
        """
                    if death == True:
                        print "From what I Understand,",person,"has died is this correct?"
                        user_input = raw_input()
                        useablestring()
                        if user_input in agreeing_keywords:
                            print"I am so sorry for their loss."
                            print"I recomend that you help them out through these tough times. It might not seem like much, but people need other people to help them through tough times."
                        if user_input in disagreeing_keywords: 
                            print 'Im sorry for thinking this'
                    if angry == True:
                        print"From what I understand your friend seems angry. Is this true?"
                        user_input = raw_input()
                        useablestring()
                        if user_input in agreeing_keywords:
                            print"""Often in depression, especialy in male depression, sadness can turn into rage or anger.
                                Anger, substance abuse and risk taking are epecialy prominant in male depression.
                                This is because it can be seen as not manely to cry or show other signs of depression.
                                I recomend talking to them on how it is ok to talk about their feelings and recomend a therappist.
                                """
                        
                    else:
                        print"""
                         I recomend telling your friend that When he is feeling low, its easy to get caught up in believing that bad things are 
        happening because of you. Dont allow yourself to believe that youre a victim. You 
        have the power to choose how you react to problems  and thats the most powerful 
        thing of all.
        """
                    time.sleep(7)    
            if user_input in disagreeing_keywords:
                print "Well, thats all I can do. Have a great day!"
            elif new_word not in agreeing_keywords:
                if new_word not in disagreeing_keywords:
                    print"Is that a yes or a no?"
                    user_input= raw_input()
                    if user_input == "yes":
                        agreeing_keywords.append(new_word)
                    if user_input == "no":
                        disagreeing_keywords.append(new_word)
                    print"Thank you for teaching me a new word!"
        if user_input in bad_keywords:
            print "It's OK to feel this way. There is hope for feeling better."
            user_input = raw_input ("Would you like to talk about it?: ")
            useablestring()
            if user_input in agreeing_keywords:
                print "So what is going on?: "
                user_input = raw_input()
                story_list = user_input.split(" ")
                user_story = [item.lower() for item in story_list]
                user_story = [re.sub(pattern, '', item) for item in user_story]
                if user_story[0] == "nothing":
                     print """"It is posible that you are experienceing a horomone inbalance. I recomend if you havent already, go visit a doctor and see what they tell you.
                     If you already have, I recommend checking out the advice or links tab for some more help."""
                    
                else:
                    while index < len(user_story):
                        if user_story[index] in bad_keywords:
                            if user_story[index-1] == "always":
                                repeat_sad = True
                                bad_counter += 1
                        if user_story[index] in good_keywords:
                            if user_story[index-1] in disagreeing_keywords:
                                bad_counter += 1
                            else:
                                good_counter += 1
                        if user_story[index] == "died":
                            if user_story[index-1] in pronoun_list:
                                person = user_story[index-1]
                                death = True
                        if user_story[index] in angry_keywords:
                            if user_story[index-1] == "is":
                                angry = True
                            if user_story[index-1] == "always":
                                angry = True
                            if user_input[index-1] in pronoun_list:
                                angry = True
                        if user_story[index] == "kill":
                            if user_story[index+1] in self_keywords:
                                suicide = True
                            if user_story[index+1] in pronoun_list:
                                murder = True
                        if user_story[index] == "bullied":
                            bullied = True
                        index += 1
                    if bullied == True:
                        print"From what I understand you are getting bullied. Is that true?"
                        user_input=raw_input()
                        if user_input in agreeing_keywords:
                            print"""when getting bullied it is important to understand the seriousness of the situation. 
                            it is entirely posible a joke went to far and a sime request to stop may be enough.
                            in serious cases it is nessesary to get someone of higher authority to intervene.
                            Dont let this situation to affect your mood. only you are in control of your emotions."""
                    if murder == True:
                        print"from what I understand you want to kill someone, is this true?"
                        user_input=raw_input()
                        if user_input in agreeing_keywords:
                            print"if you are serious about this go talk to a therapist. murder is never ok or justifiable and is a serious capital crime."
                        if user_input in disagreeing_keywords:
                            print"I am sorry for thinking this."
                    if suicide == True:
                        print"""
                        Suicide is never the answer. Life never has no meaning anymore and there is always a point or a reason to live.
                        Friends and family are always there to talk to you. Dont feel like even if you have made past mistakes that they wolnt help you.
                        there is always hope somewhere, there is always someone to talk to. if you feel up to it there are several links and phone numbers under the links catagory.
                        """
                        index += 1
                    if repeat_sad == True:
                        print""" 
                            
                         A lot of bad moods are worsened by the fact that you keep thinking about them, and 
        feeling sorry for yourself. Stop being so concerned with how you feel. Youll never 
        change things by getting stuck in thinking about them  take action instead, to make 
        things better.
        """
                    
                    if bad_counter > good_counter:
                        print """
                        Its very difficult to be depressed if you can write a long list of all the things you love in 
        your life. Not so much a mental trick as a realization of what youre very lucky to have 
        despite this tough time youre going through.
        """
                    if death == True:
                        print "From what I Understand,",person,"has died is this correct?"
                        user_input = raw_input()
                        useablestring()
                        if user_input in agreeing_keywords:
                            print"I am so sorry for your loss."
                            print"I recomend that you find someone to help you out through these tough times. It might not seem like much, but people need other people to help them through tough times."
                        if user_input in disagreeing_keywords: 
                            print 'i am sorry for thinking this.'
                    if angry == True:
                        print"from what i understand you seems angry. is this true?"
                        user_input = raw_input()
                        useablestring()
                        if user_input in agreeing_keywords:
                            print"""often in depression, especialy in male depression, sadness can turn into rage or anger.
                                Anger, substance abuse and risk taking are epecialy prominant in male depression.
                                this is because it can be seen as not manely to cry or show other signs of depression.
                                it is ok to talk about their feelings and I recomend to talk to a therapist.
                                """
                        
                    else:
                        print"""
                         When youre feeling low, its easy to get caught up in believing that bad things are 
        happening because of you. Dont allow yourself to believe that youre a victim. You 
        have the power to choose how you react to problems  and thats the most powerful 
        thing of all.
        """
                    time.sleep(7)
            if user_input in disagreeing_keywords:
                print"Before one can become better in life, one might need to look back and realize why "
                print "Do you feel like there is a reason why you feel this way or do you feel",feeling,"for no reason?:(yes or no reason) "
                user_input = raw_input()
                useablestring()
                if user_input in agreeing_keywords:
                    print "its fine that you dont want to talk about it, but it is good that you acknowledge that you are",feeling
                    user_input = raw_input("Do you know a friend who is sad?: ")
                    useablestring()
                    if user_input in agreeing_keywords:
                        print "So what is going on with them?: "
                        user_input = raw_input()
                        story_list = user_input.split(" ")
                        user_story = [item.lower() for item in story_list]
                        user_story = [re.sub(pattern, '', item) for item in user_story]
                        if user_story[0] == "nothing":
                             print """it is posible that they are experienceing a horomone imbalance. I recommend if they haven't already, go tell them to visit a doctor and see what they tell them.
                             if you already have, I recomend checking out the advice or links tab for some more help."""
                            
                        else:
                            while index < len(user_story):
                                if user_story[index] in bad_keywords:
                                    if user_story[index-1] == "always":
                                        repeat_sad = True
                                        bad_counter += 1
                                if user_story[index] in good_keywords:
                                    if user_story[index-1] in disagreeing_keywords:
                                        bad_counter += 1
                                    else:
                                        good_counter += 1
                                if user_story[index] == "died":
                                    if user_story[index-1] in pronoun_list:
                                        person = user_story[index-1]
                                        death = True
                                if user_story[index] in angry_keywords:
                                    if user_story[index-1] == "is":
                                        angry = True
                                    if user_story[index-1] == "always":
                                        angry = True
                                    if user_input[index-1] in pronoun_list:
                                        angry = True
                                if user_story[index] == "kill":
                                    if user_story[index+1] in self_keywords:
                                        suicide = True
                                    if user_story[index+1] in pronoun_list:
                                        murder = True
                                if user_story[index] == "bullied":
                                    bullied = True
                                index += 1
                            if bullied == True:
                                print"from what i understand your friend is getting bullied. is that true?"
                                user_input=raw_input()
                                if user_input in agreeing_keywords:
                                    print"""when getting bullied it is important to understand the seriousness of the situation. 
                                    it is entirely posible a joke went to far and a sime request to stop may be enough.
                                    in serious cases it is nessesary to get someone of higher authority to intervene.
                                    Dont let this situation to affect your mood. only you are in control of your emotions."""
                            if murder == True:
                                print"from what i understand your friend wants to kill someone, is this true?"
                                user_input=raw_input()
                                if user_input in agreeing_keywords:
                                    print"if they are serious about this i reccomend calling the police even if they are your best friend. murder is never ok or justifiable."
                                if user_input in disagreeing_keywords:
                                    print"I am sorry for thinking this."
                            if suicide == True:
                                print"""
                                Suicide is never the answer.life never has no meaning anymore and there is always a point or a reason to live.
                                Friends and family are always there to talk to you. Dont feel like even if you have made past mistakes that they wolnt help you.
                                there is always hope somewhere, there is always someone to talk to. if you feel up to it there are several links and phone numbers under the links catagory.
                                """
                                index += 1
                            if repeat_sad == True:
                                print""" 
                                    I recomend telling your friend that
                                 A lot of bad moods are worsened by the fact that you keep thinking about them, and 
                feeling sorry for yourself. Stop being so concerned with how you feel. Youll never 
                change things by getting stuck in thinking about them  take action instead, to make 
                things better.
                """
                            
                            if bad_counter > good_counter:
                                print """
                                I recoment telling your friend that Its very difficult to be depressed if you can write a long list of all the things you love in 
                your life. Not so much a mental trick as a realization of what youre very lucky to have 
                despite this tough time youre going through.
                """
                            if death == True:
                                print "from what I Understand,",person,"has died is this correct?"
                                user_input = raw_input()
                                useablestring()
                                if user_input in agreeing_keywords:
                                    print"I am so sorry for their loss."
                                    print"I recommend that you help them out through these tough times. It might not seem like much, but people need other people to help them through tough times."
                                if user_input in disagreeing_keywords: 
                                    print 'im sorry for thinking this'
                            if angry == True:
                                print"from what i understand your friend seems angery. is this true?"
                                user_input = raw_input()
                                useablestring()
                                if user_input in agreeing_keywords:
                                    print"""often in depression, especialy in male depression, sadness can turn into rage or anger.
                                        Anger, substance abuse and risk taking are epecialy prominant in male depression.
                                        this is because it can be seen as not manely to cry or show other signs of depression.
                                        I recomend talking to them on how it is ok to talk about their feelings and recomend a therappist.
                                        """
                                
                            else:
                                print"""
                                 I recomend telling your friend that When youre feeling low, its easy to get caught up in believing that bad things are 
                happening because of you. Dont allow yourself to believe that youre a victim. You 
                have the power to choose how you react to problems  and thats the most powerful 
                thing of all.
                """
                    if user_input in disagreeing_keywords:
                        print """well thats all i can do thank you for talking"""
                
                if user_input == "noreason":
                    print """it is posible that you are experienceing a horomone inbalance. I recomend if you havent already, you go visit a doctor and see what they tell you.
                    if you already have, I recomend checking out the advice or links tab for some more help."""
                time.sleep(7)
        if feeling not in good_keywords:
            if feeling not in bad_keywords:
                print"Unfortunatly I dont know what that word means. Does that mean you're more on the happy side or on the sad side?: "
                user_input = raw_input()
                useablestring()
                if user_input == "sad":
                    bad_keywords.append(feeling)
                    print "Thank you for teching me a new word. "
                    time.sleep(4)
                if user_input == "happy":
                    good_keywords.append(feeling)
                    print "Thanks for teaching me a new word."
                    time.sleep(4)
        print"Thank you for talking!"
        repeat_sad = False
        death = False
        angry = False
        suicide = False
        murder = False
        bullied = False
        time.sleep(3)
        print "Congratulations for getting an achievement: The talker"
        achievements = achievements +1 
        if achievements == 1:
            print """
             _________________  
            |     Tier 1      |
            |                 |
            | CONGRATULATIONS |
            |                 |
            |_________________|
"""
        if achievements == 2:
            print """

                    ___________ 
          ______   |   Tier 2  |   ______
         |      |__|           |__|      |  
         |       _CONGRATULATIONS_       |  
         |______|  |           |  |______|
                   |___________| 
"""
        if achievements == 3:
            print """


       Tier 3                 
                   ( )   
       _______    / / 
 ( )  |\      \  / /
  \ \_| \______\/_/
   \__) |       |
      | |       |
      \ |       |
       \|_______|
        | |   \ |
       ( (    | |
        \ \   | |
        ( )   | |
              ( ) 
CONGRATULATIONS THIS IS THE FINAL TIER!
"""
    if user_input == "music":
        sys.stdout.write("\033[F")
        print """Here are some links to some music for you to listen to:
            https://www.youtube.com/watch?v=fDP0gqIHVI8
            https://www.youtube.com/watch?v=qpf1ALd7eA8
            https://www.youtube.com/watch?v=AmqDOA-JALg"""
        time.sleep(7)
    if user_input == "stories":
        sys.stdout.write("\033[F")
        print"                             Here are some stories: "
      
        print"""Cates Holderness: 
              I've been dealing with major depression my entire adult life. In high school I fought my parents
              to let me see a therapist, and when I finally saw one before my senior year of high school, I was  
              diagnosed with major depression, OCD, and social anxiety disorder. Senior year was tough - I
              made excuses to friends as to why I was busy every Tuesday afternoon because I was
              embarrassed to say I was in therapy. I confided in a few close friends who were supportive, but
              frankly I was relieved to leave thought things would change, and that my depression would disappear because I was finally
              away from my hometown baggage. I was wrong.
              I saw a school counselor my freshman year at college, but I was too distracted by the newness of
              it all to really focus on my mental health. The summer after freshman year, my depression
              returned in full force. Upon returning to school for the first semester of my sophomore year, I
              was unable to recognize that my depression had completely incapacitated me. I attempted suicide
              soon after the semester began, the only reason I survived is because my friends realized there
              was something wrong with me that night. Afterwards, I dropped out of school and returned home
              to get the help I so desperately needed.
              I went through four different therapists and five different medications before I found the
              combination that worked for me, and when that happened it was not like magic, it wasn't like a
              beam of sunlight breaking through the clouds. It was like trudging up a mountain pass, swamped
              in mud and ice with an 80-pound weight around my neck. But finally I reached the peak, and 
              started down an easier path. There are still many days that I force myself uphill again, but now
              my pack is a little lighter, I have the tools to make the going a little easier, and I know that I have
              loved ones who have and will continue to carry me on days when I just can't walk anymore. I 
              always start hiking again the next morning. And I'm proud of myself.
              """
        user_input = raw_input("Do you want to read another story?: ")
        if user_input in agreeing_keywords:
            print"""Anonymous:
              A month before I was born, my grandfather died. My grandmother was suicidal. She moved in 
              with my parents and they all waited for me.
              When I was born, my grandmother said, "You saved my life." It's one of the first things I 
              remember her telling me. So there's that.
              Some say it's not right to tell people that it is selfish to kill themselves, but honestly, that was the 
              only thing that kept me from trying a few times. I'm sorry.
              couldn't do that to my boyfriend, my friends, or my siblings, or even to my parents, who back
              then I mostly blamed for the crazy in my brain.
              Whatever kooky body chemistry we all have brought me, brought us all, to the brink. I 
              wanted to figure out a fix for us. But I was so tired.
              One day, I saw a random ad for a depression study at a hospital, and despite my inability to 
              follow through on anything at the time, I went. I went back.
              It saved me.
              """ 
            user_input = raw_input("Do you want to read another story?: ")
            if user_input in agreeing_keywords:
                print"""Anonymous:
              When I was 9, I was the victim of a vicious sexual assault by a friend's older brother. For years
              after that I was depressed. I kept it a secret, and was afraid to tell anyone for fear of being
              ostracized and treated differently. I felt alone, and since I had no one to talk to about it, I suffered 
              in silence. When I was 15, I made a conscious decision to take my own life.
              I knew that my dad kept a revolver in his nightstand. It was a Saturday in the spring, and my 
              parents went to the local fair for the afternoon. I took my dad's revolver to our back patio and 
              readied myself. As I was taking the gun out of its sheath, I heard a car pull into my parents' 
              driveway. This spooked me, so I hid the gun, and found out it was my aunt coming to drop 
              something off. After she left I put the gun back, went into the house, and cried. I saw it as a sign 
              from God that I was not meant to die that day. I was still extremely bothered by what had 
              happened to me as a child. A few years later, with the help of a friend, I was able to tell my
              parents about the assault. What helped me the most through my feelings and stages of utter 
              despair was talking to other survivors who had been the victims of similar attacks.
              There are many people who have been assaulted as children, I came to find out. I initially talked 
              to a friend's sister who had been sexually abused as a child, as well. Over the years I have talked 
              to many other people, and it was so uplifting to know that I was not alone. For me, the cure was 
              talking to others. No matter how bad it may seem, or how alone you may feel, others are there to 
              help. By the grace of God and good people, I was able to get through that trying time in my life.
              """
                user_input = raw_input("Do you want to read another story?: ")
                if user_input in agreeing_keywords:
                    print"""John Stanton:
              KT, Grandpa Ed, Josh. The names scroll through my head. Every day I think their names. KT,
              Grandpa Ed, Josh. It's not a voluntary thing. They, and others, burned their names into my brain 
              during the most traumatic year and a half of my life.
              Suicide is like that. It scars those it leaves behind. Open, festering wounds, yearning for some 
              way to go back and undo the damage. But you can't. It's the most terrible kind of permanence 
              that exists
              For many of us, myself included, thoughts of suicide are simply a part of life. This horrible, 
              gaping hole that seemingly has no way of being filled. Like some kind of singularity, it 
              draws us in. Inescapable
              And then one day, you feel true pain. The pain of your best friend choosing to leave you; of the
              punk-rock icon and father figure of a generation deciding to end it all; of the gentlest, most
              caring soul you've ever known succumbing to their own pain. KT, Grandpa Ed, Josh.
              That pain is truly unbearable, because you know, no matter what, you must endure the pain of
              having lost people. No matter how weary, no matter how tired you are, you can't put that on yet
              another person.
              To do so would be to dismiss their pain. To diminish their pain. To reject the one thing that
              keeps those you have loved, and lost, alive: your memories.
              So you soldier on. Every day, silently, unwillingly saying their names. And your one, your only
              respite, are the friends who walk that path with you.
              KT, Grandpa Ed, Josh. Given the chance, each of them would undo their decision in a heartbeat. 
              They would never leave us if they knew the price we pay. KT, Grandpa Ed, Josh.
              They didn't know. But now you do. Tell a friend. A family member. A complete stranger. Tell
              me if you want. Because it can never be worse than what you'll leave behind.
              I know, because of KT, Grandpa Ed, Josh, and all those who've gone home too soon of their own accord.
              """
                    time.sleep(15)
                    print "Congradulations for getting an achievement: The Reader"
                    achievements = achievements +1 
                    if achievements == 1:
                        print """
             _________________  
            |     Tier 1      |
            |                 |
            | CONGRATULATIONS |
            |                 |
            |_________________|
"""
                    if achievements == 2:
                        print """

                    ___________ 
          ______   |   Tier 2  |   ______
         |      |__|           |__|      | 
         |       _CONGRATULATIONS_       |  
         |______|  |           |  |______|
                   |___________| 
"""
                    if achievements == 3:
                        print """


       Tier 3                 
                   ( )   
       _______    / / 
 ( )  |\      \  / /
  \ \_| \______\/_/
   \__) |       |
      | |       |
      \ |       |
       \|_______|
        | |   \ |
       ( (    | |
        \ \   | |
        ( )   | |
              ( ) 
CONGRATULATIONS THIS IS THE FINAL TIER!
"""
                    
                  
    if user_input == "view achievements":
   
   
        print """
             _________________  
            |     Tier 1      |
            |                 |
            | CONGRATULATIONS |
            |                 |
            |_________________|
"""
        print """

                    ___________ 
          ______   |   Tier 2  |   ______
         |      |__|           |__|      | 
         |       _CONGRATULATIONS_       |  
         |______|  |           |  |______|
                   |___________| 
"""

        print """


       Tier 3                 
                   ( )   
       _______    / / 
 ( )  |\      \  / /
  \ \_| \______\/_/
   \__) |       |
      | |       |
      \ |       |
       \|_______|
        | |   | |
       ( (    | |
        \ \   | |
        ( )   | |
               ( ) 
CONGRATULATIONS THIS IS THE FINAL TIER!
"""