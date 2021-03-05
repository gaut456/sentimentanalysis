import matplotlib.pyplot as plt
import numpy
#%matplotlib inline
class analysis():
	pchar=["Hurray","Yeah","Wow","amazing","delighted","joy"]
	ichar=["calm","cool","relax","chill","soothing"]
	nchar=["OhNo","sad","gloomy","angry","lost","bad"]
	p_stack = []
	i_stack = []
	n_stack = []

	def __init__(self,li):
		self.li=li
	def reaction(self):
		for i in self.li:
			res=i.split()
			for j in res:
				print(j)
				if j in self.pchar:
					self.p_stack.append(j)
				elif j in self.ichar:
					self.i_stack.append(j)
				elif j in self.nchar:
					self.n_stack.append(j)
	def cal_percent(self):
		self.pnum=len(self.p_stack)
		self.inum=len(self.i_stack)
		self.nnum=len(self.n_stack)
		self.per_p=len(self.p_stack)*100/len(self.li)
		self.per_i=len(self.i_stack)*100/len(self.li)
		self.per_n=len(self.n_stack)*100/len(self.li)
		print("% of positivity is:",self.per_p)
		print("% of neutrality is:",self.per_i)
		print("% of negativity is:",self.per_n)
	def _count(self):
		print("total number of positive characters:",self.pnum)
		print("total number of neutral characters:",self.inum)
		print("total number of negative characters:",self.nnum)
	def _plot(self):
		self.x=numpy.array(['positive count','neutral count','negative count'])
		self.y=numpy.array([self.pnum,self.inum,self.nnum])
		plt.bar(self.x,self.y,label='reaction_count',color='red',width=0.2)
		plt.legend()
		plt.show()
		portion=[self.pnum,self.inum,self.nnum]
		reactions=['positive','neutral','negative']
		plt.subplots()
		plt.pie(portion,labels=reactions)
		plt.legend(loc="upper right")
		plt.show()


l=analysis(["i am a geek","she is cool","and i hate that","cool man","That is amazing","oh WOW","my bad"])
l.reaction()
l.cal_percent()
l._plot()
