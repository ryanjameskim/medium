#Produces graphs for Uniswap v3 Medium article

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.markers

#X * Y = K curve
ETH = np.linspace(.1, 5, 50)
px = 3000 / ETH
bounded_px = 3000/ETH[6:15]

#Plotting with Labels
fig = plt.figure()
plt.plot(ETH, px, label='v2: X*Y = 3000') 
plt.plot(ETH[6:15], bounded_px, label='v3: bounded liquidity') 
plt.scatter(1,3000,marker='x',color='black', label='Current Price') 
plt.scatter(3000/2000, 2000, marker=matplotlib.markers.CARETLEFT, color='red', label='Lower Bound')
plt.scatter(3000/4500, 4500, marker=matplotlib.markers.CARETRIGHT, color='green', label='Upper Bound')

#Figure titles and labels
plt.title('Uniswap V3 versus V2 graphs')
plt.xlabel('ETH')
plt.ylabel('USDC')
plt.legend(loc='upper right')

#Show
plt.show()

#Holdings and Portfolio Values over Price Range Graph
fig, axs = plt.subplots(1, 2)

#Constants and calculations
k = 3000 
L = k**.5
upper_bound = 4500
lower_bound = 2000
L_div_Pb = L / (upper_bound**.5)
L_times_Pa = L * (lower_bound**.5)

real_y_needed = k - ((k / lower_bound) ** .5) * lower_bound
real_x_needed = 1 - (k / upper_bound) ** .5

eth_scaling_factor = 1 / real_x_needed
usd_scaling_factor = k / real_y_needed

##Alice Holdings##
alice_eth = np.linspace(0,2.25, 100) 
alice_usdc = ((k  / ((alice_eth / eth_scaling_factor) + L_div_Pb)) - L_times_Pa) * usd_scaling_factor

axs[0].scatter(1,3000,label='Starting Point')
axs[0].plot(alice_eth, alice_usdc, label = 'Alice v3 Portfolio')
axs[0].scatter(2.225,0,  marker='x', color='red', label='Alice @ ETH 2,000')
axs[0].scatter(0,6674,  marker='x', color='green', label='Alice @ ETH 4,500')

##Bob Holdings##
bob_k = 3000
bob_px = np.linspace(lower_bound, upper_bound, 100)
bob_usdc = (bob_k * bob_px) ** .5
bob_eth = (bob_k / bob_px) ** .5

axs[0].plot(bob_eth, bob_usdc, label='Bob v2 Portfolio')
axs[0].scatter(1.225,2449, marker='X', color='purple', label='Bob @ ETH 2,000')
axs[0].scatter(0.816,3674, marker='X', color='cyan', label='Bob @ ETH 4,500')

#Graph title and labels
axs[0].legend(loc='upper right')
axs[0].set(xlim=(0, 2.4), ylim=(0,7000))
axs[0].set_xlabel('ETH holdings')
axs[0].set_ylabel('USDC holdings')
axs[0].title.set_text('Changes in Holdings over Price Range (2000, 4500)')

##Portfolio value comparison
relevant_pxes = np.linspace(lower_bound, upper_bound, 100)

#Static portfolio
static_port = 1*relevant_pxes + k

#Alice
alice_relevant_eth = (real_x_needed - (1 - (k/relevant_pxes)**.5)) * eth_scaling_factor
alice_relevant_usdc = (real_y_needed - (k - (k*relevant_pxes)**.5)) * usd_scaling_factor
alice_port = alice_relevant_eth * relevant_pxes + alice_relevant_usdc

#Bob
bob_port = relevant_pxes * (bob_k / relevant_pxes) ** .5 + (bob_k * relevant_pxes) ** .5

axs[1].plot(relevant_pxes, static_port, label='Static Portfolio')
axs[1].plot(relevant_pxes, alice_port, label='Alice Portfolio')
axs[1].plot(relevant_pxes, bob_port, label='Bob Portfolio')

#Impermanent loss labels
axs[1].plot([2000,2000],[4899,4449], '--', color='red', label='Alice Impermanet Loss')
axs[1].plot([4500,4500],[7348,6674], '--', color='red')
axs[1].plot([2000,2000],[5000,4899], linestyle='dotted', color='red', label='Bob Impermanet Loss')
axs[1].plot([4500,4500],[7500,7348], linestyle='dotted', color='red')

#Graph Title and Lables
axs[1].legend(loc='upper left')
axs[1].set_xlabel('ETH Price Range')
axs[1].set_ylabel('Portfolio Values')
axs[1].title.set_text('Portfolio Value over Price Range (2000, 4500)')

#Plot show
plt.show()

#With Options Hedge (terminal value)
relevant_pxes_expand = np.linspace(lower_bound-500, upper_bound+500, 200) #Expand graph area

strike = 3000
option_cost = 1265
call_pnl = .55 * np.maximum(relevant_pxes_expand - strike, 0)
put_pnl = .55 * np.maximum(strike - relevant_pxes_expand, 0)

alice_eth_max = (real_x_needed - (1 - (k/lower_bound) ** .5 )) * eth_scaling_factor
alice_relevant_eth_expand = np.minimum((real_x_needed - (1 - (k/relevant_pxes_expand)**.5)) * eth_scaling_factor, alice_eth_max)
alice_relevant_eth_expand = np.maximum(alice_relevant_eth_expand, 0)

alice_usdc_max = (real_y_needed - (k - (k*upper_bound)**.5)) * usd_scaling_factor
alice_relevant_usdc_expand = np.minimum((real_y_needed - (k - (k*relevant_pxes_expand)**.5)) * usd_scaling_factor, alice_usdc_max)
alice_relevant_usdc_expand = np.maximum(alice_relevant_usdc_expand, 0)

alice_port_no_hedge = alice_relevant_eth_expand * relevant_pxes_expand + alice_relevant_usdc_expand
alice_port_expand = alice_relevant_eth_expand * relevant_pxes_expand + alice_relevant_usdc_expand + call_pnl + put_pnl
alice_port_option_cost = alice_port_expand - option_cost
static_port_expand = relevant_pxes_expand + 3000


fig = plt.figure()
plt.plot(relevant_pxes_expand, alice_port_no_hedge, label='Alice UnHedged Portfolio')
plt.plot(relevant_pxes_expand, alice_port_expand, label='Alice Hedged Portfolio')
plt.plot(relevant_pxes_expand, static_port_expand, label='Static Portfolio')
plt.plot(relevant_pxes_expand, alice_port_option_cost, label='Alice Hedged Portfolio w/ Cost')

plt.arrow(4500, 7500, 0, -1000, width=50, color='red')
plt.text(4600,7000, 'options', color='red')
plt.text(4600,6750, 'premium', color='red')

plt.legend()
plt.title('Alice Hedged Portfolio Value over Price Ranges')
plt.xlabel('ETH Price Range')
plt.ylabel('Portfolio Value')

plt.show()