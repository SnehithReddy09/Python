

class stat:
    def dsmean(self, data, frequency):
        res_list=[]
        if all(isinstance(i, int) or isinstance(i,float) for i in data) and all(isinstance(i, int) for i in frequency):
            if(len(data))==len(frequency):
                for i in range(0, len(data)):
                    res_list.append(data[i] * frequency[i])

                return (sum(res_list)/sum(frequency))
            else:
                return("Error 1")
        else:
            return("error 2")
    
        
    def mode(self,data,frequency):
        ma=frequency.index(max(frequency)) 
        return data[ma] 
    def dsmode(self,data):
        count = 0
        num = data[0]
        for i in data:
            mode = data.count(i)
            if(mode > count):
                count = mode
                num = i
        return (num)
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

    def gmean(self,data):
        x=1
        for i in data:
            x*=i 
        return (x**(1/len(data)))

    def hmean(self,data):
        x=0
        for i in data:
            x += 1 / i 
        return len(data)/x

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
#print(o.dsmean(data,frequency))
#print(o.dsmedian(data))
#print(o.dsmode(data))
print(o.gmean(data))
print(o.hmean(data))
print(o.dvariance(data))