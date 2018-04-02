import gym
env = gym.make('Blackjack-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        if observation[2] == True:
            print("오... 나한텐 사용가능한 ACE가 있어...!")
            if observation[0] < 19:
                action = 1
        else:
            if observation[0] < 17:
                action = 1
            else:
                action = 0

        if action==1:
            print("내 카드 합이",observation[0],"이니 카드 한 장 더 주세요.")
        else:
            print("내 카드 합이",observation[0],"이니 그만 받을래요.")
        observation, reward, done, info = env.step(action)
        if action==1:
            print("카드를 한 장 받아서 카드합이",observation[0],"가 되었습니다.")
        if action==0:
            print("카드를 홀드하여 최종 카드합이",observation[0],"가 되었습니다.")
        if done:
            if observation[0]>21:
                print("카드 합이 21을 넘어서 망했습니다. 졌어요.")
            elif reward == 0:
                print("내 카드는",observation[3],"최종합",observation[0],"; 상대 카드는",observation[4],"최종합",observation[5],"; 비겼습니다.")
            elif reward == 1.0:
                print("내 카드는", observation[3], "최종합", observation[0], "; 상대 카드는", observation[4], "최종합", observation[5],"; 이겼습니다.")
            elif reward == 1.5:
                print("카드 두장으로 블랙잭 완성!")
            else:
                print("내 카드는", observation[3], "최종합", observation[0], "; 상대 카드는", observation[4], "최종합", observation[5],"; 졌습니다.")
            print("Episode finished after {} timesteps".format(t+1))
            break