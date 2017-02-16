// Auto-generated. Do not edit!

// (in-package learn_ball.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class ballCor {
  constructor() {
    this.x = 0;
    this.y = 0;
    this.radius = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ballCor
    // Serialize message field [x]
    bufferInfo = _serializer.int64(obj.x, bufferInfo);
    // Serialize message field [y]
    bufferInfo = _serializer.int64(obj.y, bufferInfo);
    // Serialize message field [radius]
    bufferInfo = _serializer.int64(obj.radius, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ballCor
    let tmp;
    let len;
    let data = new ballCor();
    // Deserialize message field [x]
    tmp = _deserializer.int64(buffer);
    data.x = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [y]
    tmp = _deserializer.int64(buffer);
    data.y = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [radius]
    tmp = _deserializer.int64(buffer);
    data.radius = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'learn_ball/ballCor';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd7c108a8b71c29a2d00a2f240bd5f683';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 x
    int64 y
    int64 radius
    
    `;
  }

};

module.exports = ballCor;
