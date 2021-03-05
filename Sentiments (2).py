#!/usr/bin/env python
# coding: utf-8

# In[46]:


import matplotlib.pyplot as plt


# In[75]:


#Entering user given comment
chat = input("Enter your comment:")

print(chat)


# In[48]:


#data pre processing
input_comment = chat.lower()
word_list = input_comment.split()
number_of_words = len(word_list)
print(number_of_words)


# In[49]:


Positive = ["happy", "wow", "awww", "hurray", "excited" , "blessed", "pleasure", "brilliant", "facinating", "superb",
            "facinated", "amazing", "beautiful", "love", "loves", "loved", "positive", "wonderful", "incredible",
            "excellent", "fantastic", "perfect", "genius", "funny", "insightfull", "glad"]

Neutral = ["calm", "chilling", "okay", "fair", "unbiased", "cool", "impartial"]

Negative = ["Oh no", "Uff", "angry", "sick", "okay", "heartbroken", "lost", "unhappy", "unrealistic", "sorry", "stupid",
           "shallow", "worst", "miserable", "annoying", "hated", "poor", "unlikable", "dumb", "dull", "sadly", "mistake",
            "stuck", "badly", "awfull", "horrible", "hated", "negative", "dislike", "dull", "mess"]


# In[69]:


count=0
for i in Positive:
    if (input_comment.find(i) != -1):
        count+=1
        print("His sentiments are Positive")
    p_percent=round((count*100)/number_of_words, 2)
print("Person is %.2f percent Positive" %(p_percent))


# In[70]:


count=0
for j in Neutral:
    if (chat.find(j) != -1):
        count+=1
        print("His sentiments are Neutral")
    n_percent=round((count*100)/number_of_words,2)
print("person is %.2f percent Neutral" %(n_percent))


# In[78]:


count=0
for k in Negative:
    if (chat.find(k) != -1):
        count+=1
        print("His sentiments are Negative")
    s_percent=round((count*100)/number_of_words, 2)
print("Person is %.2f percent Negative" %(s_percent))


# In[79]:


list_1=[p_percent, n_percent, s_percent]
print(list_1)
normal =100-sum(list_1)
print("Remaining %.2f pecent comment is normal." %(normal))


# In[84]:


#Visualization through Pie Chart
portion=p_percent, n_percent, s_percent, normal
activities=["positivity", "neutrality", "negativity", "normal"]
plt.subplots()
plt.pie(portion, labels=activities, colors=['green','yellow','red','blue'])
plt.legend(loc="lower right")
plt.show()


# In[85]:


#Visualization through Bar graph
plt.subplot(111)
x=['positive', 'neutral', 'negative', 'normal']
y=p_percent, n_percent, s_percent, normal
plt.bar(x, y, label="Analysis Data", color="purple", width=0.3)
plt.legend(loc="upper right")
plt.show()


# In[ ]:




