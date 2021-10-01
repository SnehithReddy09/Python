'''
PROGRAM DESCRIPITON: 
	Write a python program to calculate mean, variance, median, mode, geometric mean and hormonic mean.
'''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 21-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

class stat:
    #Calculating for mean
    def dsmean(self, data, frequency):
        res_list=[]
        # checking whether all elements in data are either int or floast and elements in frequency are int only.
        if all(isinstance(i, int) or isinstance(i,float) for i in data) and all(isinstance(i, int) for i in frequency):
            if(len(data))==len(frequency):
                for i in range(0, len(data)):
                    res_list.append(data[i] * frequency[i])
                # returning the mean value for given data.
                return (sum(res_list)/sum(frequency))
            else:
                return("Error 1")
        else:
            return("error 2")
    
    # calculating the frequently occured value in the data if frequency is given.
    def mode(self,data,frequency):
        ma=frequency.index(max(frequency)) 
        return data[ma] 
    
    # calculating  the frequently occured value in the data if data is given without frequency.
    def dsmode(self,data):
        count = 0
        num = data[0]
        for i in data:
            mode = data.count(i)
            if(mode > count):
                count = mode
                num = i
        return (num)
    
    #calculating the median of data.
    def dsmedian(self, data):
        data.sort()
        #even number data 
        if(len(data)%2 ==0):
            self.number = (len(data)+1)/2
            return (data[int(self.number)-1])
        #odd number dataset 
        elif(len(data)%2!=0):
            self.number=(len(data)+1)/2
            return (data[int(self.number)-1])

    #calculating the geometric mean of the data nth root(product of all values), where n is total number of values.
    def gmean(self,data):
        x=1
        for i in data:
            x*=i 
        return (x**(1/len(data)))

    # calculating the hormonic mean of the data n/(sum of reciprocals of values).
    def hmean(self,data):
        x=0
        for i in data:
            x += 1 / i 
        return len(data)/x

    # calculating the variance of data.
    def dvariance(self,data):
        m=sum(data)/len(data)
        v=0 
        for i in data:
            y=i-m 
            v+=(y)**(1/2)
        return v/len(data)


data=[1,2,3,4,6]
frequency=[4,6,7]
o=stat()
print(o.dsmean(data,frequency))
print(o.dsmedian(data))
print(o.dsmode(data))
print(o.gmean(data))
print(o.hmean(data))
print(o.dvariance(data))
