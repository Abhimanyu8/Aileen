import aiml
import os.path
import sys
import renpy.exports as renpy


class AimlBot:
	brainFileName = "standard.brn"
	kernel = aiml.Kernel()
	botName = "Aileen"
	botMaster = "A.L.I.C.E. AI Foundation"
	Birthday = "Sep 06, 2006"
	Boyfriend = "Uncle Mugen"

	def __init__(self):
		self.kernel.verbose(False)
		self.kernel.setBotPredicate("name", self.botName)
		self.kernel.setBotPredicate("master", self.botMaster)
		self.kernel.setBotPredicate("birthday", self.Birthday)
		self.kernel.setBotPredicate("boyfriend", self.Boyfriend)

		if renpy.loadable(self.brainFileName):
		    self.kernel.bootstrap(brainFile = os.path.join(renpy.config.gamedir,self.brainFileName))
		else:
		    self.kernel.bootstrap(learnFiles = os.path.join(renpy.config.gamedir,"std-startup.xml"), commands = "load aiml b")
		    self.kernel.saveBrain(os.path.join(renpy.config.gamedir,self.brainFileName))

	# runs bot on input and returns answer
	def run(self, inputString):
		answer =  self.kernel.respond(inputString) # second argument is string
		#self.kernel.saveBrain(self.brainFileName)
		return answer
		