import tkinter

class Entry(tkinter.Tk):
    location="hello"
    order="1"
    regression_type="0"
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Banker's algorithm")
        self.geometry("500x500")
        

        label = tkinter.Label(text="Enter No.Of Resources :")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=200)
        label.pack(fill=tkinter.BOTH, expand=1)

        self.entry = tkinter.Entry()
        self.entry.pack(fill=tkinter.BOTH, expand=0)

        labe2 = tkinter.Label(text="Enter No.Of Processes :")
        labe2.config(justify=tkinter.LEFT)
        labe2.config(wrap=200)
        labe2.pack(fill=tkinter.BOTH, expand=1)

        self.entry1 = tkinter.Entry()
        self.entry1.pack(fill=tkinter.BOTH, expand=0)
        
        labe3 = tkinter.Label(text="Enter Claim Vector")
        labe3.config(justify=tkinter.LEFT)
        labe3.config(wrap=200)
        labe3.pack(fill=tkinter.BOTH, expand=1)

        self.entry3 = tkinter.Entry()
        self.entry3.pack(fill=tkinter.BOTH, expand=0)

        labe4 = tkinter.Label(text="Enter Allocated Resource Table :")
        labe4.config(justify=tkinter.LEFT)
        labe4.config(wrap=200)
        labe4.pack(fill=tkinter.BOTH, expand=1)

        self.entry4 = tkinter.Entry()
        self.entry4.pack(fill=tkinter.BOTH, expand=0)

        labe5 = tkinter.Label(text="Enter Maximum Claim Table :")
        labe5.config(justify=tkinter.LEFT)
        labe5.config(wrap=200)
        labe5.pack(fill=tkinter.BOTH, expand=1)

        self.entry5 = tkinter.Entry()
        self.entry5.pack(fill=tkinter.BOTH, expand=0)

        button = tkinter.Button(text="compute", command=self.Bankers_algo,bg = "blue")
        button.pack(fill=tkinter.BOTH, expand=0)
        
        labe6 = tkinter.Label(text="results:")
        labe6.config(justify=tkinter.LEFT)
        labe6.config(wrap=200)
        labe6.pack(fill=tkinter.BOTH, expand=1)



    def Bankers_algo(self):
        count = 0
        safe = False

        r= int(self.entry.get())

        p = int(self.entry1.get())

        
        curr = []
        max_claim = []
        avl = []
        alloc = []
        max_res = []
        running = []


        for i in range(0,p):
            running.append(1)
            count = count + 1
        #max claim vector
            
        claim_vector = self.entry3.get()
        claim_vector_list=claim_vector.split(",")
        print(len(claim_vector_list))
        for i in range(0,r):
            claim_vector_list[i] = int(claim_vector_list[i])
        print(claim_vector_list)
        max_res= claim_vector_list
            
        resource_table = self.entry4.get()
        resource_table_list= resource_table.split(",")
        length= p*r
        for i in range (0,length):
            resource_table_list[i]= int(resource_table_list[i])

        for i in range(0,p):
            curr.append([])

        for i in range(0,p):
            for j in range(0,r):
                curr[i].append(j)
                curr[i][j] = 0

        for i in range(0,p):
            pos= i*r
            for j in range(0,r):
                pos= pos+j
                curr[i][j] = resource_table_list[pos]

        print("Enter Maximum Claim Table : ")

        claim_table = self.entry5.get()
        claim_table_list = claim_table.split(",")
        length= p*r
        for i in range (0,length):
            claim_table_list[i] = int(claim_table_list[i])
        for i in range(0,p):
            max_claim.append([])

        for i in range(0,p):
            for j in range(0,r):
                max_claim[i].append(j)
                max_claim[i][j] = 0

        for i in range(0,p):
            pos= i*r
            for j in range(0,r):
                pos=pos+j
                max_claim[i][j] = claim_table_list[pos]
        print(claim_table_list)
        print("The Claim Vector is ",max_res)
        print("The Allocate Resource Table is ",curr)
        print("The Maximum Claim Table is ",max_claim)
        
        for z in range(0,r):
            alloc.append(0)

        for i in range(0,p):
            for j in range(0,r):
                alloc[j] = alloc[j] + curr[i][j]

        print("Allocated Resources are : ", alloc)
        for i in range(0,r):
            avl.append(0)
        for u in range(0,r):
            avl[u] = max_res[u] - alloc[u]

        print("Available resources are : ",avl)
        output= "results:\n"
        while count!=0:
            safe = False
            for i in range(0,p):
                if running[i]:
                    exec = 1
                    for j in range(0,r):
                        if (max_claim[i][j] - curr[i][j] > avl[j]):
                            exec = 0
                            break

                    if(exec):
                        output=output+"Process Is Executing "+str(i+1)
                        running[i] = 0
                        count = count - 1
                        safe = True
                        for j in range(0,r):
                            avl[j] = avl[j] + curr[i][j];
                        break

            if not safe :
                output=output+"The Processes Are In Unsafe State\n"
                break

            if safe:
                output=output+"The Process Is In Safe Sate"
            print(output)
            labe6.config(text=output)
            print("Available Vector is ",avl)
            print(output)
            labe6.config(text=output)
if __name__ == "__main__":
    application = Entry()
    application.mainloop()


