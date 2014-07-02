
'''
MAP Client Plugin Step
'''

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint


class pointsCloudDictMakerStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting points
    for new steps.
    '''

    def __init__(self, location):
        super(pointsCloudDictMakerStep, self).__init__('points Cloud Dict Maker', location)
        self._configured = True # A step cannot be executed until it has been configured.
        self._category = 'General'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#pointclouddict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#pointclouddict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#pointcoordinates'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'string'))

        self._pointsDict = None
        self._points = None
        self._pointsName = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._pointsDict==None:
            self._pointsDict = {}
        self._pointsDict[self._pointsName] = self._points
        self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 1:
            self._pointsDict = dataIn # ju#pointsclouddict
        elif index == 2:
            self._points = dataIn # ju#pointscoordinates
        else:
            self._pointsName = dataIn # string

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._pointsDict # ju#pointsclouddict

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        pass

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return 'pointsCloudDictMaker' # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass # TODO: Must actually set the step's identifier here

    def serialize(self, location):
        '''
        Add code to serialize this step to disk.  The filename should
        use the step identifier (received from getIdentifier()) to keep it
        unique within the workflow.  The suggested name for the file on
        disk is:
            filename = getIdentifier() + '.conf'
        '''
        pass

    def deserialize(self, location):
        '''
        Add code to deserialize this step from disk.  As with the serialize 
        method the filename should use the step identifier.  Obviously the 
        filename used here should be the same as the one used by the
        serialize method.
        '''
        pass

