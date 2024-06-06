/**
 * Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, headingColor, axisColor, shadeColor, borderColor;

  cardColor = config.colors.white;
  headingColor = config.colors.headingColor;
  axisColor = config.colors.axisColor;
  borderColor = config.colors.borderColor;

  document.addEventListener('DOMContentLoaded', function() {
      // Get all product elements
      const productElements = document.querySelectorAll('#product-data .product');

      // Initialize total volumes for each warehouse
      let totalVolumeA = 0, totalVolumeB = 0, totalVolumeC = 0, totalVolumeD = 0;

      productElements.forEach(element => {
          const qty = parseFloat(element.querySelector('.product-qty').textContent);
          const volume = parseFloat(element.querySelector('.product-volume').textContent);
          const location = element.querySelector('.product-location').textContent;

          const totalVolume = qty * volume;

          if (location === 'A') totalVolumeA += totalVolume;
          else if (location === 'B') totalVolumeB += totalVolume;
          else if (location === 'C') totalVolumeC += totalVolume;
          else if (location === 'D') totalVolumeD += totalVolume;
      });

      // Warehouse capacities
      const capacity = 1000;

      // Calculate the percentages for each warehouse
      const percentageA = (totalVolumeA / capacity) * 100;
      const percentageB = (totalVolumeB / capacity) * 100;
      const percentageC = (totalVolumeC / capacity) * 100;
      const percentageD = (totalVolumeD / capacity) * 100;

      // Total Revenue Report Chart - Bar Chart
      const totalRevenueChartEl = document.querySelector('#totalRevenueChart'),
          totalRevenueChartOptions = {
          series: [{
              data: [percentageA, percentageB, percentageC, percentageD] // The data for the bar chart
          }],
          chart: {
              type: 'bar',
              height: 300,
              toolbar: { show: false }
          },
          plotOptions: {
              bar: {
                  horizontal: true,
                  borderRadius: 4,
                  dataLabels: {
                      position: 'top', // Show data labels on top of bars
                  },
              }
          },
          dataLabels: {
              enabled: true,
              formatter: function (val) {
                  return val.toFixed(0) + "%";
              },
              offsetX: -6,
              style: {
                  fontSize: '12px',
                  colors: ['#fff']
              }
          },
          xaxis: {
              categories: ['A', 'B', 'C', 'D'],
              max: 100,
              labels: {
                  formatter: function (val) {
                      return val + "%";
                  }
              }
          },
          yaxis: {
              title: {
                  text: 'Warehouses'
              }
          },
          fill: {
              colors: ['#7367F0'] // Adjust the color as per your design
          },
          title: {
              text: '',
              align: 'left',
              style: {
                  fontSize: '18px',
                  fontWeight: 'bold',
                  color: '#263238'
              }
          },
          grid: {
              borderColor: '#f1f1f1'
          },
          states: {
              hover: {
                  filter: {
                      type: 'none'
                  }
              },
              active: {
                  filter: {
                      type: 'none'
                  }
              }
          }
      };

      if (typeof totalRevenueChartEl !== undefined && totalRevenueChartEl !== null) {
          const totalRevenueChart = new ApexCharts(totalRevenueChartEl, totalRevenueChartOptions);
          totalRevenueChart.render();
      }
  });

  document.addEventListener('DOMContentLoaded', function() {
    // Select all product quantity elements
    const productQtyElements = document.querySelectorAll('.product-qty');

    // Calculate the total product quantity
    let totalProductQty = 0;
    productQtyElements.forEach(element => {
        totalProductQty += parseFloat(element.textContent);
    });

    // Calculate the capacity percentage
    const capacityPercentage = (totalProductQty / 255) * 100;

    // Growth Chart - Radial Bar Chart
    const growthChartEl = document.querySelector('#growthChart'),
        growthChartOptions = {
        series: [capacityPercentage.toFixed(2)],
        labels: ['Utilization'],
        chart: {
            height: 240,
            type: 'radialBar'
        },
        plotOptions: {
            radialBar: {
                size: 150,
                offsetY: 10,
                startAngle: -150,
                endAngle: 150,
                hollow: {
                    size: '55%'
                },
                track: {
                    background: cardColor,
                    strokeWidth: '100%'
                },
                dataLabels: {
                    name: {
                        offsetY: 15,
                        color: headingColor,
                        fontSize: '15px',
                        fontWeight: '600',
                        fontFamily: 'Public Sans'
                    },
                    value: {
                        offsetY: -25,
                        color: headingColor,
                        fontSize: '22px',
                        fontWeight: '500',
                        fontFamily: 'Public Sans'
                    }
                }
            }
        },
        colors: [config.colors.primary],
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                shadeIntensity: 0.5,
                gradientToColors: [config.colors.primary],
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 0.6,
                stops: [30, 70, 100]
            }
        },
        stroke: {
            dashArray: 5
        },
        grid: {
            padding: {
                top: -35,
                bottom: -10
            }
        },
        states: {
            hover: {
                filter: {
                    type: 'none'
                }
            },
            active: {
                filter: {
                    type: 'none'
                }
            }
        }
    };
    if (typeof growthChartEl !== undefined && growthChartEl !== null) {
        const growthChart = new ApexCharts(growthChartEl, growthChartOptions);
        growthChart.render();
    }
});


  // Profit Report Line Chart
  // --------------------------------------------------------------------
  const profileReportChartEl = document.querySelector('#profileReportChart'),
    profileReportChartConfig = {
      chart: {
        height: 80,
        // width: 175,
        type: 'line',
        toolbar: {
          show: false
        },
        dropShadow: {
          enabled: true,
          top: 10,
          left: 5,
          blur: 3,
          color: config.colors.warning,
          opacity: 0.15
        },
        sparkline: {
          enabled: true
        }
      },
      grid: {
        show: false,
        padding: {
          right: 8
        }
      },
      colors: [config.colors.warning],
      dataLabels: {
        enabled: false
      },
      stroke: {
        width: 5,
        curve: 'smooth'
      },
      series: [
        {
          data: [110, 270, 145, 245, 205, 285]
        }
      ],
      xaxis: {
        show: false,
        lines: {
          show: false
        },
        labels: {
          show: false
        },
        axisBorder: {
          show: false
        }
      },
      yaxis: {
        show: false
      }
    };
  if (typeof profileReportChartEl !== undefined && profileReportChartEl !== null) {
    const profileReportChart = new ApexCharts(profileReportChartEl, profileReportChartConfig);
    profileReportChart.render();
  }

  // Order Statistics Chart
  // --------------------------------------------------------------------
  const chartOrderStatistics = document.querySelector('#orderStatisticsChart'),
    orderChartConfig = {
      chart: {
        height: 165,
        width: 130,
        type: 'donut'
      },
      labels: ['Electronic', 'Sports', 'Decor', 'Fashion'],
      series: [85, 15, 50, 50],
      colors: [config.colors.primary, config.colors.secondary, config.colors.info, config.colors.success],
      stroke: {
        width: 5,
        colors: cardColor
      },
      dataLabels: {
        enabled: false,
        formatter: function (val, opt) {
          return parseInt(val) + '%';
        }
      },
      legend: {
        show: false
      },
      grid: {
        padding: {
          top: 0,
          bottom: 0,
          right: 15
        }
      },
      plotOptions: {
        pie: {
          donut: {
            size: '75%',
            labels: {
              show: true,
              value: {
                fontSize: '1.5rem',
                fontFamily: 'Public Sans',
                color: headingColor,
                offsetY: -15,
                formatter: function (val) {
                  return parseInt(val) + '%';
                }
              },
              name: {
                offsetY: 20,
                fontFamily: 'Public Sans'
              },
              total: {
                show: true,
                fontSize: '0.8125rem',
                color: axisColor,
                label: 'Weekly',
                formatter: function (w) {
                  return '38%';
                }
              }
            }
          }
        }
      }
    };
  if (typeof chartOrderStatistics !== undefined && chartOrderStatistics !== null) {
    const statisticsChart = new ApexCharts(chartOrderStatistics, orderChartConfig);
    statisticsChart.render();
  }

  // Income Chart - Area chart
  // --------------------------------------------------------------------
  const incomeChartEl = document.querySelector('#incomeChart'),
    incomeChartConfig = {
      series: [
        {
          data: [24, 21, 30, 22, 42, 26, 35, 29]
        }
      ],
      chart: {
        height: 215,
        parentHeightOffset: 0,
        parentWidthOffset: 0,
        toolbar: {
          show: false
        },
        type: 'area'
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        width: 2,
        curve: 'smooth'
      },
      legend: {
        show: false
      },
      markers: {
        size: 6,
        colors: 'transparent',
        strokeColors: 'transparent',
        strokeWidth: 4,
        discrete: [
          {
            fillColor: config.colors.white,
            seriesIndex: 0,
            dataPointIndex: 7,
            strokeColor: config.colors.primary,
            strokeWidth: 2,
            size: 6,
            radius: 8
          }
        ],
        hover: {
          size: 7
        }
      },
      colors: [config.colors.primary],
      fill: {
        type: 'gradient',
        gradient: {
          shade: shadeColor,
          shadeIntensity: 0.6,
          opacityFrom: 0.5,
          opacityTo: 0.25,
          stops: [0, 95, 100]
        }
      },
      grid: {
        borderColor: borderColor,
        strokeDashArray: 3,
        padding: {
          top: -20,
          bottom: -8,
          left: -10,
          right: 8
        }
      },
      xaxis: {
        categories: ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          show: true,
          style: {
            fontSize: '13px',
            colors: axisColor
          }
        }
      },
      yaxis: {
        labels: {
          show: false
        },
        min: 10,
        max: 50,
        tickAmount: 4
      }
    };
  if (typeof incomeChartEl !== undefined && incomeChartEl !== null) {
    const incomeChart = new ApexCharts(incomeChartEl, incomeChartConfig);
    incomeChart.render();
  }

  // Expenses Mini Chart - Radial Chart
  // --------------------------------------------------------------------
  const weeklyExpensesEl = document.querySelector('#expensesOfWeek'),
    weeklyExpensesConfig = {
      series: [65],
      chart: {
        width: 60,
        height: 60,
        type: 'radialBar'
      },
      plotOptions: {
        radialBar: {
          startAngle: 0,
          endAngle: 360,
          strokeWidth: '8',
          hollow: {
            margin: 2,
            size: '45%'
          },
          track: {
            strokeWidth: '50%',
            background: borderColor
          },
          dataLabels: {
            show: true,
            name: {
              show: false
            },
            value: {
              formatter: function (val) {
                return '$' + parseInt(val);
              },
              offsetY: 5,
              color: '#697a8d',
              fontSize: '13px',
              show: true
            }
          }
        }
      },
      fill: {
        type: 'solid',
        colors: config.colors.primary
      },
      stroke: {
        lineCap: 'round'
      },
      grid: {
        padding: {
          top: -10,
          bottom: -15,
          left: -10,
          right: -10
        }
      },
      states: {
        hover: {
          filter: {
            type: 'none'
          }
        },
        active: {
          filter: {
            type: 'none'
          }
        }
      }
    };
  if (typeof weeklyExpensesEl !== undefined && weeklyExpensesEl !== null) {
    const weeklyExpenses = new ApexCharts(weeklyExpensesEl, weeklyExpensesConfig);
    weeklyExpenses.render();
  }
})();
