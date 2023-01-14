import simplegui
import random

cardsize=[50,100]
halfwidth=cardsize[0]/2
margin=2
cardfontsize=50


# helper function to initialize globals
def new_game():
    global cardlist,exposed,state,oldcards,turncount
    
    state=0
    oldcards=[]
    turncount=0   
    
    cardlist1=range(0,8)
    cardlist2=range(0,8)
    cardlist=cardlist1+cardlist2
    random.shuffle(cardlist)
    exposed=[False for i in range(16)]

     
# define event handlers
def mouseclick(pos):
    global state,oldcards,turncount
    
    click_pos = list(pos)
    cardcount=0    
    for card in cardlist:
        if click_pos[0]<(cardcount+1)*cardsize[0] and click_pos[0]>=cardcount*cardsize[0]:
             if not(exposed[cardcount]):
                if state == 0:
                    exposed[cardcount]=True
                    oldcards.append([cardcount,card])
                    state = 1
                    turncount+=1
                elif state == 1:
                    exposed[cardcount]=True
                    oldcards.append([cardcount,card])
                    state = 2
                else:
                    if oldcards[-1][1]!=oldcards[-2][1]:
                        exposed[oldcards[-1][0]]=False
                        exposed[oldcards[-2][0]]=False
                    exposed[cardcount]=True
                    oldcards.append([cardcount,card])
                    turncount+=1
                      
                    state = 1
            
        cardcount+=1
        
                  
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = "+str(turncount))
    cardcount=0    
    for card in cardlist:
        canvas.draw_line([cardcount*cardsize[0]+ halfwidth, 0], [cardcount*cardsize[0]+ halfwidth, cardsize[1]], cardsize[0]-margin, 'Green')
        if exposed[cardcount]:
            cardtext=str(card)
            canvas.draw_text(cardtext,
                         (cardcount*cardsize[0]+(cardsize[0]-frame.get_canvas_textwidth(cardtext, cardfontsize,'serif'))/2,(cardsize[1]+0.75*cardfontsize)/2),
                         cardfontsize, 'Black', 'serif')
        cardcount+=1
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things going
new_game()
frame.start()

