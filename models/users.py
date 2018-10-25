class users():
    
    users_list=[]

    def __init__(self,full_name,email,password,confirm_pwd):
        self.full_name=full_name
        self.email=email
        self.role='Store Attendant'
        self.password=password
        self.confirm_pwd=confirm_pwd
        self.user_id=len(self.users_list)+1
    
    def add_user(self):
        user={'user_id':self.user_id, 'user_fullname':self.full_name, 'user_email':self.email, 'user_role':self.role, 'user_password':self.password}
        if self.password==self.confirm_pwd:
            self.users_list.append(user)
            return 'User has been registered'   
        else:
            return 'Passwords do not match'  

    def get_users(self):
        if self.users_list:
            another_users_list=[]
            user_dict={}
            for u in self.users_list:
                user_dict.update({'User full name':u['user_fullname'], 'Email':u['user_email'], 'User role':u['user_role']})
                another_users_list.append(user_dict.copy())
            return another_users_list
        else:
            return 'There are no users yet'


        
        
        
        