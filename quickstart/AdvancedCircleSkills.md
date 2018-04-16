# 圈选技巧

##一.如何利用通配符进行圈选

GrowingIO支持使用通配符进行同类页面的匹配，以帮助您更灵活更方便的进行数据的统计和分析。目前GrowingIO支持利用星号进行url的通配。

您可以在进行圈选时，对页面的路径进行通配，已达到圈选同类页面的目的。在圈选时的使用通配符的位置如下：  
![](通配.jpg)

###「*」的典型用途有如下:

 - 放在Path的尾部，通配所有具有相似结构的path  
例如：project/projectid/*
 - 作为path中的某一段，匹配该段path的所有内容  
例如：project/*/segmentations

###具体的用例：
**1.放在Path的尾部，通配所有具有相似结构的path**      
在GrowingIO的数据分析界面中，有如下结构的path：

 - project/projectid/segmentations
 - project/projectid/retention
 - project/projectid/overview
 - .......

每个url都代表着特定的功能页面，例如segmentations代表用户分群，retention代表留存，overview则是概览。  如果想要了解，一个项目的所有页面的浏览量，这个时候只需要在路径中使用通配符就能够解决问题了

    project/projectid/*

这样，这个通配的页面标签就包含了所有「www.growingio.com/project/projectid/...」的页面。您就可以直接利用这个标签来进行数据分析了


**2.作为path中的某一段，匹配该段path的所有内容**  
如果要对「用户分群」功能的使用情况进行分析，则需要进行另外一种通配  
按照严格匹配来定义页面，您需要将多个标签进行加和才能够得到用户分群的总浏览情况，因为每个项目有不同的projectid，例如：

 - project/projectid1/segmentations
 - project/projectid2/segmentations
 - project/projectid3/segmentations

在使用页面通配符时，您只需在路径中使用通配符:

    /project/*/segmentations

这样便可以将所有项目中的用户分群页面，都一起进行数据统计和分析了

 
