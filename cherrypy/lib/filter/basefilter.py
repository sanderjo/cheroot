"""
Copyright (c) 2004, CherryPy Team (team@cherrypy.org)
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, 
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, 
      this list of conditions and the following disclaimer in the documentation 
      and/or other materials provided with the distribution.
    * Neither the name of the CherryPy Team nor the names of its contributors 
      may be used to endorse or promote products derived from this software 
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

class RequestHandled(Exception): pass

class BaseInputFilter(object):
    """
    Base class for input filters. Derive new filter classes from this, then
    override some of the methods to add some side-effects.
    """
    def afterRequestHeader(self):
        """ Called after the request header has been read/parsed"""
        pass

    def afterRequestBody(self):
        """ Called after the request body has been read/parsed"""
        pass

class BaseOutputFilter(object):
    """
    Base class for output filters. Derive new filter classes from this, then
    override some of the methods to add some side-effects.
    """
    def beforeResponse(self):
        """ Called before starting to write response """
        pass

    def afterResponse(self):
        """ Called after writing the response (header & body included) """
        pass

    def beforeErrorResponse(self):
        """ Called before starting to write response, after _cpOnError has
            been called
        """
        pass

    def afterErrorResponse(self):
        """ Called after writing the response, after _cpOnError has
            been called
        """
        pass

