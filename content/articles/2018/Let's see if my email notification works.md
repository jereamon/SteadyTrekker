Title: Let's see if my email notification works
Date: 2018-05-29 11:32:44
PostImage: article_images/default-post-thumbnail.jpg
Status: draft



Yep, this is more of a test than anything. I recently set up the functionality to allow people to subscribe to my email list and get notified when I post something new. What an excellent learning experience that was. A bit of a frustrating experience at that. It was my first introduction to HTML email. Which I assumed would be simple, just like writing HTML/CSS for a web page. But of course, I was wrong. I had no idea how limited you are with the structure of your email and the styling you are able to use.

First off, having gained my web dev skills at the end of 2017 I intently studied flexbox and CSS grid. That being said many email clients don't support either. Some have issues with divs. To promote cross-compatibility between email clients you will likely have to resort to the use of tables. Good old table rows and table data. What a good time. I didn't realize how much I relied on flexbox until it was taken away from me. My expediency with it keeps me from using anything else. So, in this case, probably my fault for not branching out.

<img class="size-medium wp-image-697 aligncenter" src="/images/article_images/2018/06/dennis-buchner-489213-unsplash-300x190.jpg" alt="" width="300" height="190" />

Once you've gotten over the structural issues you run into a styling nightmare. All styles need to be written inline. You can't have an external stylesheet and style tags in your head will be removed by most email clients. This being my introduction to HTML emails, I thought would code it from scratch real quick. No big deal. Instead, I found myself feeling very limited and quickly concluded that external tools to aid in creation are necessary for quick production. On the flip side write it from scratch and have fun getting more familiar with tools you might not use very much.

That's all for now. like I said at the top this is more of a test than anything. We'll see if my wonderfully simple HTML email notification gets sent out once I post this.