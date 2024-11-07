sen_ = input("Double Space Detector :- write a sentence :  ")
out_ =(sen_.find ("  "))
if out_ == -1:
    print("""No double space detected - Done        //
                                             \\    //
                                              \\  //
                                               \\//
     """)
else:
    print("""Double space detected - \\    //  
                                      \\  //
                                       \\//
                                        \/
                                        ||
                                       //\\    
                                      //  \\        
                                     //    \\    
            """)    

