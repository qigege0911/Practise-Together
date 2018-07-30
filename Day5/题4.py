import re

'请用正则表达式将下面字符串里面的英文行分离出来，保存在列表，列表里面的每一个元素为一行英文' \
'(包括标点符号)' \

s = '''
And now, the end is near;
现在，我的末日将近，
And so I face the final curtain.
面临人生的最后落幕，
My friend, I'll make it clear,
我的朋友，我要说个清楚，
I'll state my case, of which I'm certain.
向你讲述我的人生之路。
I've lived a life that's full.
我活过一个充实的人生，
I've traveled each and every highway;
我经历过每一段路途，
And more, much more I did,
而更重要的是，
I did it my way.
我用自己的方式。
Regrets, I've had a few;
遗憾，也有一些吧，
But then again, too few to mention.
算不上多，不值一提。
I did what I had to do
我做了该做的一切，
And saw it through without exemption.
洞悉世事，不求赦免。
I planned each charted course;
我规划过每一段人生，
Each careful step along the by way,
每一个细微的脚步，
and more, much more than this,
而更重要的是，
I did it my way.
我用自己的方式。
Yes, there were times, I'm sure you knew
是的，你知道有些时候，
When I bit off more than I could chew.
我曾背负不能承受之重，
But through it all, when there was doubt,
但自始至终，就算充满疑惑，
I ate it up and spit it out.
我还是克服困难战胜了它。
I faced it all and I stood tall;
我挺直身躯，勇敢面对，
And did it my way.
用我自己的方式。
I’ve loved, I’ve laughed and cried.
我曾经爱过，笑过，哭过，
I’ve had my fill; my share of losing.
我曾经满足，也曾经失落，
And now, as tears subside,
现在，当泪水慢慢沉淀，
I find it all so amusing.
我发现原来可以一笑置之。
To think I did all that;
想到我所做过的一切，
And may I say - not in a shy way,
我可以说，毫不羞愧地说，
No, oh no not me,
我没有虚度，
I did it my way.
我用自己的方式。
For what is a man, what has he got?
男人究竟是什么，拥有什么？
If not himself, then he has naught.
除了自己，我们一无所有。
To say the things he truly feels;
说出心里最真实的感受，
And not the words of one who kneels.
而不是那些身不由己的话。
The record shows I took the blows -
时间证明，我经受住了磨难，
And did it my way!
用我自己的方式！
Yes, it was my way.
没错，这就是我的方式。
'''
result=re.findall(r'\n([a-zA-Z\s\',;.!?-]+)\n',s)
print(result)