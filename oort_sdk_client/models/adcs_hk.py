# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oort_sdk_client.configuration import Configuration


class AdcsHk(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'control_error_angle_deg': 'float',
        'acs_mode_active': 'str',
        'euler_angles': 'AdcsEulerT',
        'control_error_q': 'AdcsQuatT',
        'lat_deg': 'float',
        'q_bo_est': 'AdcsQuatT',
        'latlontrack_lat': 'float',
        'lease_active': 'int',
        'lon_deg': 'float',
        'eclipse_flag': 'int',
        'q_bi_est': 'AdcsQuatT',
        'latlontrack_lon': 'float',
        'r_eci': 'AdcsXyzFloatT',
        'altitude': 'float',
        'latlontrack_body_vector': 'AdcsXyzFloatT',
        'omega_bo_est': 'AdcsXyzFloatT',
        'acs_mode_cmd': 'str',
        'v_eci': 'AdcsXyzFloatT',
        'qcf': 'AdcsQuatT',
        'lease_time_remaining': 'int',
        'unix_timestamp': 'float',
        'omega_bi_est': 'AdcsXyzFloatT',
        'control_error_omega': 'AdcsXyzFloatT',
        'r_ecef': 'AdcsXyzFloatT'
    }

    attribute_map = {
        'control_error_angle_deg': 'control_error_angle_deg',
        'acs_mode_active': 'acs_mode_active',
        'euler_angles': 'euler_angles',
        'control_error_q': 'control_error_q',
        'lat_deg': 'lat_deg',
        'q_bo_est': 'q_bo_est',
        'latlontrack_lat': 'latlontrack_lat',
        'lease_active': 'lease_active',
        'lon_deg': 'lon_deg',
        'eclipse_flag': 'eclipse_flag',
        'q_bi_est': 'q_bi_est',
        'latlontrack_lon': 'latlontrack_lon',
        'r_eci': 'r_eci',
        'altitude': 'altitude',
        'latlontrack_body_vector': 'latlontrack_body_vector',
        'omega_bo_est': 'omega_bo_est',
        'acs_mode_cmd': 'acs_mode_cmd',
        'v_eci': 'v_eci',
        'qcf': 'qcf',
        'lease_time_remaining': 'lease_time_remaining',
        'unix_timestamp': 'unix_timestamp',
        'omega_bi_est': 'omega_bi_est',
        'control_error_omega': 'control_error_omega',
        'r_ecef': 'r_ecef'
    }

    def __init__(self, control_error_angle_deg=None, acs_mode_active=None, euler_angles=None, control_error_q=None, lat_deg=None, q_bo_est=None, latlontrack_lat=None, lease_active=None, lon_deg=None, eclipse_flag=None, q_bi_est=None, latlontrack_lon=None, r_eci=None, altitude=None, latlontrack_body_vector=None, omega_bo_est=None, acs_mode_cmd=None, v_eci=None, qcf=None, lease_time_remaining=None, unix_timestamp=None, omega_bi_est=None, control_error_omega=None, r_ecef=None, local_vars_configuration=None):  # noqa: E501
        """AdcsHk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._control_error_angle_deg = None
        self._acs_mode_active = None
        self._euler_angles = None
        self._control_error_q = None
        self._lat_deg = None
        self._q_bo_est = None
        self._latlontrack_lat = None
        self._lease_active = None
        self._lon_deg = None
        self._eclipse_flag = None
        self._q_bi_est = None
        self._latlontrack_lon = None
        self._r_eci = None
        self._altitude = None
        self._latlontrack_body_vector = None
        self._omega_bo_est = None
        self._acs_mode_cmd = None
        self._v_eci = None
        self._qcf = None
        self._lease_time_remaining = None
        self._unix_timestamp = None
        self._omega_bi_est = None
        self._control_error_omega = None
        self._r_ecef = None
        self.discriminator = None

        if control_error_angle_deg is not None:
            self.control_error_angle_deg = control_error_angle_deg
        if acs_mode_active is not None:
            self.acs_mode_active = acs_mode_active
        if euler_angles is not None:
            self.euler_angles = euler_angles
        if control_error_q is not None:
            self.control_error_q = control_error_q
        if lat_deg is not None:
            self.lat_deg = lat_deg
        if q_bo_est is not None:
            self.q_bo_est = q_bo_est
        if latlontrack_lat is not None:
            self.latlontrack_lat = latlontrack_lat
        if lease_active is not None:
            self.lease_active = lease_active
        if lon_deg is not None:
            self.lon_deg = lon_deg
        if eclipse_flag is not None:
            self.eclipse_flag = eclipse_flag
        if q_bi_est is not None:
            self.q_bi_est = q_bi_est
        if latlontrack_lon is not None:
            self.latlontrack_lon = latlontrack_lon
        if r_eci is not None:
            self.r_eci = r_eci
        if altitude is not None:
            self.altitude = altitude
        if latlontrack_body_vector is not None:
            self.latlontrack_body_vector = latlontrack_body_vector
        if omega_bo_est is not None:
            self.omega_bo_est = omega_bo_est
        if acs_mode_cmd is not None:
            self.acs_mode_cmd = acs_mode_cmd
        if v_eci is not None:
            self.v_eci = v_eci
        if qcf is not None:
            self.qcf = qcf
        if lease_time_remaining is not None:
            self.lease_time_remaining = lease_time_remaining
        if unix_timestamp is not None:
            self.unix_timestamp = unix_timestamp
        if omega_bi_est is not None:
            self.omega_bi_est = omega_bi_est
        if control_error_omega is not None:
            self.control_error_omega = control_error_omega
        if r_ecef is not None:
            self.r_ecef = r_ecef

    @property
    def control_error_angle_deg(self):
        """Gets the control_error_angle_deg of this AdcsHk.  # noqa: E501

        Absolute control error angle   # noqa: E501

        :return: The control_error_angle_deg of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._control_error_angle_deg

    @control_error_angle_deg.setter
    def control_error_angle_deg(self, control_error_angle_deg):
        """Sets the control_error_angle_deg of this AdcsHk.

        Absolute control error angle   # noqa: E501

        :param control_error_angle_deg: The control_error_angle_deg of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._control_error_angle_deg = control_error_angle_deg

    @property
    def acs_mode_active(self):
        """Gets the acs_mode_active of this AdcsHk.  # noqa: E501

        Active ADCS mode   # noqa: E501

        :return: The acs_mode_active of this AdcsHk.  # noqa: E501
        :rtype: str
        """
        return self._acs_mode_active

    @acs_mode_active.setter
    def acs_mode_active(self, acs_mode_active):
        """Sets the acs_mode_active of this AdcsHk.

        Active ADCS mode   # noqa: E501

        :param acs_mode_active: The acs_mode_active of this AdcsHk.  # noqa: E501
        :type: str
        """

        self._acs_mode_active = acs_mode_active

    @property
    def euler_angles(self):
        """Gets the euler_angles of this AdcsHk.  # noqa: E501


        :return: The euler_angles of this AdcsHk.  # noqa: E501
        :rtype: AdcsEulerT
        """
        return self._euler_angles

    @euler_angles.setter
    def euler_angles(self, euler_angles):
        """Sets the euler_angles of this AdcsHk.


        :param euler_angles: The euler_angles of this AdcsHk.  # noqa: E501
        :type: AdcsEulerT
        """

        self._euler_angles = euler_angles

    @property
    def control_error_q(self):
        """Gets the control_error_q of this AdcsHk.  # noqa: E501


        :return: The control_error_q of this AdcsHk.  # noqa: E501
        :rtype: AdcsQuatT
        """
        return self._control_error_q

    @control_error_q.setter
    def control_error_q(self, control_error_q):
        """Sets the control_error_q of this AdcsHk.


        :param control_error_q: The control_error_q of this AdcsHk.  # noqa: E501
        :type: AdcsQuatT
        """

        self._control_error_q = control_error_q

    @property
    def lat_deg(self):
        """Gets the lat_deg of this AdcsHk.  # noqa: E501

        Subsatellite latitude, in degrees   # noqa: E501

        :return: The lat_deg of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._lat_deg

    @lat_deg.setter
    def lat_deg(self, lat_deg):
        """Sets the lat_deg of this AdcsHk.

        Subsatellite latitude, in degrees   # noqa: E501

        :param lat_deg: The lat_deg of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._lat_deg = lat_deg

    @property
    def q_bo_est(self):
        """Gets the q_bo_est of this AdcsHk.  # noqa: E501


        :return: The q_bo_est of this AdcsHk.  # noqa: E501
        :rtype: AdcsQuatT
        """
        return self._q_bo_est

    @q_bo_est.setter
    def q_bo_est(self, q_bo_est):
        """Sets the q_bo_est of this AdcsHk.


        :param q_bo_est: The q_bo_est of this AdcsHk.  # noqa: E501
        :type: AdcsQuatT
        """

        self._q_bo_est = q_bo_est

    @property
    def latlontrack_lat(self):
        """Gets the latlontrack_lat of this AdcsHk.  # noqa: E501

        latitude used for ground target tracking   # noqa: E501

        :return: The latlontrack_lat of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._latlontrack_lat

    @latlontrack_lat.setter
    def latlontrack_lat(self, latlontrack_lat):
        """Sets the latlontrack_lat of this AdcsHk.

        latitude used for ground target tracking   # noqa: E501

        :param latlontrack_lat: The latlontrack_lat of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._latlontrack_lat = latlontrack_lat

    @property
    def lease_active(self):
        """Gets the lease_active of this AdcsHk.  # noqa: E501

        Flag if a lease is currently active   # noqa: E501

        :return: The lease_active of this AdcsHk.  # noqa: E501
        :rtype: int
        """
        return self._lease_active

    @lease_active.setter
    def lease_active(self, lease_active):
        """Sets the lease_active of this AdcsHk.

        Flag if a lease is currently active   # noqa: E501

        :param lease_active: The lease_active of this AdcsHk.  # noqa: E501
        :type: int
        """

        self._lease_active = lease_active

    @property
    def lon_deg(self):
        """Gets the lon_deg of this AdcsHk.  # noqa: E501

        Subsatellite longitude, in degrees   # noqa: E501

        :return: The lon_deg of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._lon_deg

    @lon_deg.setter
    def lon_deg(self, lon_deg):
        """Sets the lon_deg of this AdcsHk.

        Subsatellite longitude, in degrees   # noqa: E501

        :param lon_deg: The lon_deg of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._lon_deg = lon_deg

    @property
    def eclipse_flag(self):
        """Gets the eclipse_flag of this AdcsHk.  # noqa: E501

        Sunlit/eclipse status of spacecraft   # noqa: E501

        :return: The eclipse_flag of this AdcsHk.  # noqa: E501
        :rtype: int
        """
        return self._eclipse_flag

    @eclipse_flag.setter
    def eclipse_flag(self, eclipse_flag):
        """Sets the eclipse_flag of this AdcsHk.

        Sunlit/eclipse status of spacecraft   # noqa: E501

        :param eclipse_flag: The eclipse_flag of this AdcsHk.  # noqa: E501
        :type: int
        """

        self._eclipse_flag = eclipse_flag

    @property
    def q_bi_est(self):
        """Gets the q_bi_est of this AdcsHk.  # noqa: E501


        :return: The q_bi_est of this AdcsHk.  # noqa: E501
        :rtype: AdcsQuatT
        """
        return self._q_bi_est

    @q_bi_est.setter
    def q_bi_est(self, q_bi_est):
        """Sets the q_bi_est of this AdcsHk.


        :param q_bi_est: The q_bi_est of this AdcsHk.  # noqa: E501
        :type: AdcsQuatT
        """

        self._q_bi_est = q_bi_est

    @property
    def latlontrack_lon(self):
        """Gets the latlontrack_lon of this AdcsHk.  # noqa: E501

        longitude used for ground target tracking   # noqa: E501

        :return: The latlontrack_lon of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._latlontrack_lon

    @latlontrack_lon.setter
    def latlontrack_lon(self, latlontrack_lon):
        """Sets the latlontrack_lon of this AdcsHk.

        longitude used for ground target tracking   # noqa: E501

        :param latlontrack_lon: The latlontrack_lon of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._latlontrack_lon = latlontrack_lon

    @property
    def r_eci(self):
        """Gets the r_eci of this AdcsHk.  # noqa: E501


        :return: The r_eci of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._r_eci

    @r_eci.setter
    def r_eci(self, r_eci):
        """Sets the r_eci of this AdcsHk.


        :param r_eci: The r_eci of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._r_eci = r_eci

    @property
    def altitude(self):
        """Gets the altitude of this AdcsHk.  # noqa: E501

        Estimated altitude of satellite in meters   # noqa: E501

        :return: The altitude of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this AdcsHk.

        Estimated altitude of satellite in meters   # noqa: E501

        :param altitude: The altitude of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._altitude = altitude

    @property
    def latlontrack_body_vector(self):
        """Gets the latlontrack_body_vector of this AdcsHk.  # noqa: E501


        :return: The latlontrack_body_vector of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._latlontrack_body_vector

    @latlontrack_body_vector.setter
    def latlontrack_body_vector(self, latlontrack_body_vector):
        """Sets the latlontrack_body_vector of this AdcsHk.


        :param latlontrack_body_vector: The latlontrack_body_vector of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._latlontrack_body_vector = latlontrack_body_vector

    @property
    def omega_bo_est(self):
        """Gets the omega_bo_est of this AdcsHk.  # noqa: E501


        :return: The omega_bo_est of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._omega_bo_est

    @omega_bo_est.setter
    def omega_bo_est(self, omega_bo_est):
        """Sets the omega_bo_est of this AdcsHk.


        :param omega_bo_est: The omega_bo_est of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._omega_bo_est = omega_bo_est

    @property
    def acs_mode_cmd(self):
        """Gets the acs_mode_cmd of this AdcsHk.  # noqa: E501

        Commanded ADCS mode   # noqa: E501

        :return: The acs_mode_cmd of this AdcsHk.  # noqa: E501
        :rtype: str
        """
        return self._acs_mode_cmd

    @acs_mode_cmd.setter
    def acs_mode_cmd(self, acs_mode_cmd):
        """Sets the acs_mode_cmd of this AdcsHk.

        Commanded ADCS mode   # noqa: E501

        :param acs_mode_cmd: The acs_mode_cmd of this AdcsHk.  # noqa: E501
        :type: str
        """

        self._acs_mode_cmd = acs_mode_cmd

    @property
    def v_eci(self):
        """Gets the v_eci of this AdcsHk.  # noqa: E501


        :return: The v_eci of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._v_eci

    @v_eci.setter
    def v_eci(self, v_eci):
        """Sets the v_eci of this AdcsHk.


        :param v_eci: The v_eci of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._v_eci = v_eci

    @property
    def qcf(self):
        """Gets the qcf of this AdcsHk.  # noqa: E501


        :return: The qcf of this AdcsHk.  # noqa: E501
        :rtype: AdcsQuatT
        """
        return self._qcf

    @qcf.setter
    def qcf(self, qcf):
        """Sets the qcf of this AdcsHk.


        :param qcf: The qcf of this AdcsHk.  # noqa: E501
        :type: AdcsQuatT
        """

        self._qcf = qcf

    @property
    def lease_time_remaining(self):
        """Gets the lease_time_remaining of this AdcsHk.  # noqa: E501

        time remaining in current ADCS lease   # noqa: E501

        :return: The lease_time_remaining of this AdcsHk.  # noqa: E501
        :rtype: int
        """
        return self._lease_time_remaining

    @lease_time_remaining.setter
    def lease_time_remaining(self, lease_time_remaining):
        """Sets the lease_time_remaining of this AdcsHk.

        time remaining in current ADCS lease   # noqa: E501

        :param lease_time_remaining: The lease_time_remaining of this AdcsHk.  # noqa: E501
        :type: int
        """

        self._lease_time_remaining = lease_time_remaining

    @property
    def unix_timestamp(self):
        """Gets the unix_timestamp of this AdcsHk.  # noqa: E501

        Unix epoch time   # noqa: E501

        :return: The unix_timestamp of this AdcsHk.  # noqa: E501
        :rtype: float
        """
        return self._unix_timestamp

    @unix_timestamp.setter
    def unix_timestamp(self, unix_timestamp):
        """Sets the unix_timestamp of this AdcsHk.

        Unix epoch time   # noqa: E501

        :param unix_timestamp: The unix_timestamp of this AdcsHk.  # noqa: E501
        :type: float
        """

        self._unix_timestamp = unix_timestamp

    @property
    def omega_bi_est(self):
        """Gets the omega_bi_est of this AdcsHk.  # noqa: E501


        :return: The omega_bi_est of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._omega_bi_est

    @omega_bi_est.setter
    def omega_bi_est(self, omega_bi_est):
        """Sets the omega_bi_est of this AdcsHk.


        :param omega_bi_est: The omega_bi_est of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._omega_bi_est = omega_bi_est

    @property
    def control_error_omega(self):
        """Gets the control_error_omega of this AdcsHk.  # noqa: E501


        :return: The control_error_omega of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._control_error_omega

    @control_error_omega.setter
    def control_error_omega(self, control_error_omega):
        """Sets the control_error_omega of this AdcsHk.


        :param control_error_omega: The control_error_omega of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._control_error_omega = control_error_omega

    @property
    def r_ecef(self):
        """Gets the r_ecef of this AdcsHk.  # noqa: E501


        :return: The r_ecef of this AdcsHk.  # noqa: E501
        :rtype: AdcsXyzFloatT
        """
        return self._r_ecef

    @r_ecef.setter
    def r_ecef(self, r_ecef):
        """Sets the r_ecef of this AdcsHk.


        :param r_ecef: The r_ecef of this AdcsHk.  # noqa: E501
        :type: AdcsXyzFloatT
        """

        self._r_ecef = r_ecef

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdcsHk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdcsHk):
            return True

        return self.to_dict() != other.to_dict()