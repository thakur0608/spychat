print 'welcome to spychat'
spy_name=raw_input('what is your name  ')
if len(spy_name)==0:
    print "enter valid name"
    exit('try again')
spy_sallutation=raw_input('what we should call you MR. OR MS.')
if len(spy_sallutation)==0:
    print"enter valid details"
    exit('try again')
spy_age=int(raw_input('what is your age'))
if spy_age<1:
    print"enter valid age"
    exit('try again')
else:
    print "hello %s  ,%s ,age:%d" %(spy_sallutation,spy_name,spy_age)
    print "glad to have you"

spy_rating=raw_input('do you want to rate us yes or no:')
if(spy_rating)=="yes":
    spy_rating=raw_input( "give rating from 1 to 5 :")
    if spy_rating>4.5:
        print "you are awesome"
        exit();
    if (spy_rating)>3 and len(spy_rating)<4.5:
        print "you arre good hope we would improve it"
    else :
        print"thank you we will try to improve"
else :
    print"hope you would enjoy time"



