import matplotlib.pyplot as plt
import lights as l
import smokemachine as sm

stgsize = 500
light_disp_size = 50
color_disp = ['red','blue','green','yellow','orange','purple','magenta','cyan']

L0 = l.Light(0.65,"blue",[250,25],[20,10,100])
L1 = l.Light(0.65,"red",[350,25],[20,10,0])

SM0 = sm.SmokeMachine([0,0])
SM1 = sm.SmokeMachine([500,0])

SM0.startSmoke()
SM1.startSmoke()

for i in range(0,10):
	L0.set_color(color_disp[i])
	L1.set_color(color_disp[-i])

	for n in range(0,10):
		SM0o= SM0.stepChange(stgsize,"right")
		SM1o = SM1.stepChange(stgsize,"left")

	fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]},
								figsize = (10,10))

	ax0.set_aspect("equal")
	ax0.fill([0,stgsize,stgsize,0],[0,10,light_disp_size,light_disp_size], color="black")
	ax0.add_patch(L0.construct_circle())
	ax0.add_patch(L1.construct_circle())

	ax1.set_aspect("equal")
	ax1.fill([0,stgsize,stgsize,0],[0,0,stgsize,stgsize], color="black")

	ax1.add_patch(L0.construct_beam(stgsize))
	ax1.add_patch(L0.construct_light(stgsize))

	ax1.add_patch(L1.construct_beam(stgsize))
	ax1.add_patch(L1.construct_light(stgsize))

	ax1.scatter(SM0o[0], SM0o[1], s = SM0o[2], c = SM0o[3], alpha = SM0o[4])
	ax1.scatter(SM1o[0], SM1o[1], s = SM1o[2], c = SM1o[3], alpha = SM1o[4])

	ax1.set_xlim(0,stgsize)
	ax1.set_ylim(0,stgsize)

	plt.suptitle("STAGEVIEW", fontsize="18")
	plt.pause(0.8)