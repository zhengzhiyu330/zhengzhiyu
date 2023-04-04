# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import re

a = os.popen(
    'curl http://172.16.1.148:8080/jenkins/view/vvmusic_ios/job/mvbox_ios_99_0_0/lastSuccessfulBuild/artifact/output/')
c = a.readlines()
print(a)
print(c)
print(type(c))
name = "Artifacts"
for x in c:
    if re.findall(name, x):
        result = x.split("mvbox_ios")
        print(result)
        nums = result[1].split("#")
        print(nums)
        num = nums[1].split(" ")
        print(num)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#test1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
