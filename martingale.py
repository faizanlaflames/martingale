""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np
# import matplotlib
# matplotlib.use('Agg') #  to stop plots from appearing in windows
import matplotlib.pyplot as plt	


num_episodes = 1000
max_spins = 300
target_winnings = 80
bankroll_limit = 256	  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "fh"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 982329219  # replace with your GT ID number  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 

    #simming the martingale strategy
def sim_episode(win_prob=18/38): 
    episode_winnings = 0
    bet_amount = 1
    winnings_history = []

    for _ in range(1000):  # maximum of 1000 spins
        if episode_winnings >= 80:
            winnings_history.append(episode_winnings)
        else:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bet_amount = 1  # reset bet amount after a win
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # double the bet after a loss
            winnings_history.append(episode_winnings)
    
    # fill remaining spins with final winnings
    winnings_history.extend([episode_winnings] * (1000 - len(winnings_history)))
    return winnings_history

    #kinda similar but with a $256 bankroll limit
def sim_with_bankroll(num_episodes, max_spins, bankroll_limit):
    all_episode_winnings = []

    for _ in range(num_episodes):
        episode_winnings = [0]
        bankroll = 0
        bet = 1

        for _ in range(max_spins):
            if bankroll <= -bankroll_limit:  # stop betting when our bankroll is depleted
                episode_winnings.append(-bankroll_limit)
                continue

            if bankroll >= target_winnings:  # stop when our target is reached
                episode_winnings.append(bankroll)
                continue

            if bet > (bankroll_limit + bankroll):  # adjust bet if it's more than bankroll
                bet = bankroll_limit + bankroll

            result = np.random.choice([-1, 1], p=[20/38, 18/38]) # using american roulette probabilities
            bankroll += bet * result
            bet = 1 if result == 1 else min(bet * 2, bankroll_limit + bankroll)  # either reset or double bet

            episode_winnings.append(bankroll)

        all_episode_winnings.append(episode_winnings) #add to winnings

    return np.array(all_episode_winnings)

# running our simulation
winnings_data = sim_with_bankroll(num_episodes, max_spins, bankroll_limit)

# calculating stats
mean_winnings = np.mean(winnings_data, axis=0)
std_winnings = np.std(winnings_data, axis=0)
median_winnings = np.median(winnings_data, axis=0)


    #experiment one, figure 1 
def plot_10_episodes():
    episodes = [sim_episode() for _ in range(10)] #ten episodes
    for i, episode in enumerate(episodes):
        plt.plot(episode, label=f'Episode {i+1}')
    
    fig_1 = plt.figure(1) 
    
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings')
    plt.title('Martingale Strategy, 10 Episodes')
   
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
   
    plt.legend()
    # plt.savefig("./images/figure1.png") 
    # plt.close(fig_1) # not using plt.show() to prevent plots from populating in windows.
    plt.show()
    
   
    #experiment one, figure 2
def plot_mean_std():
    episodes = np.array([sim_episode() for _ in range(1000)]) #1000 episodes
    mean_winnings = np.mean(episodes, axis=0)
    std_winnings = np.std(episodes, axis=0)

    fig_2 = plt.figure(2)

    columns = range(len(mean_winnings))

    plt.plot(columns, mean_winnings, label='Mean')
    plt.plot(columns, mean_winnings + std_winnings, label='Mean + Std')
    plt.plot(columns, mean_winnings - std_winnings, label='Mean - Std')

    plt.xlabel('Spin Number')
    plt.ylabel('Winnings')
    plt.title('Mean Winnings Across 1000 Episodes')
    
    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.legend()
    # plt.savefig("./images/figure2.png") 
    # plt.close(fig_2)
    plt.show()
    

    #experiment one, figure 3 
def plot_median_std():
    episodes = np.array([sim_episode() for _ in range(1000)])
    median_winnings = np.median(episodes, axis=0)
    std_winnings = np.std(episodes, axis=0)

    fig_3 = plt.figure(3)
    
    columns = range(len(median_winnings))
    
    plt.plot(columns, median_winnings, label='Median')
    plt.plot(columns, median_winnings + std_winnings, label='Median + Std')
    plt.plot(columns, median_winnings - std_winnings, label='Median - Std')
    
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings')
    plt.title('Median Winnings Across 1000 Episodes')
    
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
   
    plt.legend()
    # plt.savefig("./images/figure3.png") 
    # plt.close(fig_3)
    plt.show()
    

    #experiment two, figure 4
def plot_realistic_mean():
    fig_4 = plt.figure(4)
    
    columns = range(len(mean_winnings))
    
    plt.plot(columns, mean_winnings, label='Mean',)
    plt.plot(columns, mean_winnings + std_winnings, label='Mean + Std')
    plt.plot(columns, mean_winnings - std_winnings, label='Mean - Std')

    
    plt.xlabel("Spin Number")
    plt.ylabel("Winnings")
    plt.title("Mean Winnings Across 1000 Episodes w/ Bankroll Limit")
   
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    
    plt.legend()
    # plt.savefig("./images/figure4.png") 
    # plt.close(fig_4)
    plt.show()
     

    #experiment two, figure 5
def plot_realistic_median():
    fig_5 = plt.figure(5)
    
    columns = range(len(median_winnings))
   
    plt.plot(columns, median_winnings, label='Median',)
    plt.plot(columns, median_winnings + std_winnings, label='Median + Std')
    plt.plot(columns, median_winnings - std_winnings, label='Median - Std')
   
    plt.xlabel("Spin Number")
    plt.ylabel("Winnings")
    plt.title("Median Winnings Across 1000 Episodes w/ Bankroll Limit")
    
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    
    plt.legend()
    # plt.savefig("./images/figure5.png") 
    # plt.close(fig_5) 
    plt.show()
    
 	 	 			  		  		 	 	 			  		 			     			  	 
def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Method to test your code  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		 	 	 			  		 			     			  	 
    
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 			  		 			     			  	 
    
    # print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 			  		 			     			  	 
    # add your code here to implement the experiments  		  	   		 	 	 			  		 			     			  	 
  	
    plot_10_episodes() #figure1
    plot_mean_std() #figure2
    plot_median_std() #figure3
    plot_realistic_mean() #figure4
    plot_realistic_median()	#figure5  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 
