# | Parameter  | Default      | Description                                                                    |
# | ---------- | ------------ | ------------------------------------------------------------------------------ |
# | `*objects` | —            | Jo bhi values print karni hain, comma se separate karke likhte hain            |
# | `sep`      | `' '`        | Multiple objects ko separate karne ke liye string, default space               |
# | `end`      | `'\n'`       | Print ke end me kya lagana hai, default new line                               |
# | `file`     | `sys.stdout` | Output ka destination, console ke alawa file ya custom stream bhi ho sakta hai |
# | `flush`    | `False`      | True → buffer ko turant flush kar do (useful for real-time logging)            |

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# with open('./print_function/output.txt', 'w') as f:
#     print("Hello, it's a re-directed stream", file=f) #hum yaha par stdout ko (stream ) ko re-direct bhi kar sakte hai ;


# import time
# for i in range(3):
#     print(i, end=" ", flush=True)
#     time.sleep(1)
# # Numbers print immediately one by one


# import time
# for i in range(1, 101):
#     print(f"\rProgress: {i}%", end="", flush=True)
#     time.sleep(0.1)   #yeh main thread ko block kar raha hai sleep function ka use karke 


# for i in range(5):
#     print(i, end="")  # end="" means newline nahi hai
#     # buffer me store ho jata hai, console me turant nahi dikhega

# for i in range(5):
#     print(i, end="", flush=True)


# import time
# for i in range(5):
#     print(i, end="")
#     time.sleep(1)


# # '\r' yeh print karne k baad fir se wahi usi line par aa jata hai jaha par isne pehle print kia tha ;
# import time 


# for i in range(1,101):
#     print(f'\rprogress: {i}%' , end = "")
#     time.sleep(0.2)