import random


def create_outline():
    """
    TODO: implement your code here
    """
    
    # STEP 1
    '''
    CREATED TWO LISTS OF COURSES AND USED SET TO PRINT(RANDOM)
    '''
    
    list_of_Coures = [
        ' Introduction to Python',
        ' Tools of the Trade',
        ' How to make decisions', 
        ' How to repeat code',
        ' How to structure data', 
        ' Functions', 
        ' Modules'
                    ]
    set_list = set(list_of_Coures)
    conv_back_to_list = list(set_list)
    sorted_list = sorted(conv_back_to_list)                                                        # STEP 4
    print('Course Topics:')
    for i in sorted_list:
        print('*'+i)
    
    # STEP 2
    '''
    CREATED TWO LISTS OF PROBLEMS AND EMPTY DICT. 
    FIRST LOOP FOR KEYS AND SECOND LOOP FOR VALUES IN THE EMPTY DICT
    '''
    set_of_problems = ['Problem 1,', ' Problem 2,', ' Problem 3']
    empty = {}
    print("Problems:")
    for e in sorted_list:
        empty[e] = set_of_problems
        
    for keys, values in empty.items():
        print('*'+keys, ': ', end='')
        for value in values:
            print(value, end='')
        print()
        
    # STEP 3 
    
    '''
    CREATED MY TWO LISTS OF STUDENTS AND SORTED-STATUS
    '''
    list_of_problems = ['Problem 1', 'Problem 2', 'Problem 3']
    student_names = [
        'Nyari', 
        'Adam','
        'Siyabonga',
        'Nduduzo',
        'Sunshine',
        'Thabang'
        ]
    status_list = [
        '[GRADED]',
        '[STARTED]',
        '[COMPLETED]',
        '[GRADED]',
        '[COMPLETED]',
        '[GRADED]'
        ]   
    status_list.sort()                                                                            # STEP 4
      
    print('Student Progress:')
  
    tuples_list = []
    tuples_list = sorted(tuples_list, key=lambda tup: tup[3],reverse=True)  #
    counter = 1   
    '''
    THIS BOTTOM PART OF THE CODE, 
    I CREATED A TUPLE AND APPENED IT TO A LIST CALLED TUPLE_LIST
    '''
    for name in student_names:                                                                                         
        tupl = (name,random.choice(list_of_Coures),random.choice(list_of_problems),status_list.pop())
        tuples_list += (tupl,)
    '''
    THIS BOTTOM PART OF THE CODE PRINTS THE OUTPUT
    '''        
    for student in tuples_list:
        print(f"{str(counter)}. {student[0]} - {student[1]} - {student[2]} {student[3]}")
        counter += 1
    
    pass


if __name__ == "__main__":
    create_outline() 
